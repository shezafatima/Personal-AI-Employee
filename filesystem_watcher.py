"""
File System Watcher - Monitors Inbox folder for new files
"""
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil
import logging
from datetime import datetime


class DropFolderHandler(FileSystemEventHandler):
    """Handles file system events in the Inbox folder"""

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.inbox = self.vault_path / 'Inbox'
        self.needs_action = self.vault_path / 'Needs_Action'
        self.logger = logging.getLogger(self.__class__.__name__)

        # Ensure directories exist
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.needs_action.mkdir(parents=True, exist_ok=True)

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def on_created(self, event):
        """Called when a file is created in the watched directory"""
        if event.is_directory:
            return

        source = Path(event.src_path)

        # Ignore temporary files and hidden files
        if source.name.startswith('.') or source.name.startswith('~'):
            return

        try:
            # Wait a moment to ensure file is fully written
            import time
            time.sleep(1)

            # Copy file to Needs_Action with prefix
            dest = self.needs_action / f'FILE_{source.name}'
            shutil.copy2(source, dest)

            # Create metadata file
            self.create_metadata(source, dest)

            self.logger.info(f'Processed new file: {source.name}')

        except Exception as e:
            self.logger.error(f'Error processing file {source}: {e}')

    def create_metadata(self, source: Path, dest: Path):
        """Create a markdown metadata file for the dropped file"""
        meta_path = dest.with_suffix('.md')

        # Get file stats
        stats = source.stat()
        size_kb = stats.st_size / 1024

        content = f"""---
type: file_drop
original_name: {source.name}
size: {size_kb:.2f} KB
received: {datetime.now().isoformat()}
priority: normal
status: pending
---

## New File Dropped for Processing

**File**: {source.name}
**Size**: {size_kb:.2f} KB
**Location**: {dest}

## Suggested Actions
- [ ] Review file contents
- [ ] Determine appropriate action
- [ ] Move to /Done when complete

## Notes
Add any relevant notes or context here.
"""

        meta_path.write_text(content, encoding='utf-8')


def run_filesystem_watcher(vault_path: str):
    """Start the file system watcher"""
    handler = DropFolderHandler(vault_path)
    observer = Observer()

    inbox_path = Path(vault_path) / 'Inbox'
    observer.schedule(handler, str(inbox_path), recursive=False)

    observer.start()
    handler.logger.info(f'Watching {inbox_path} for new files...')

    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        handler.logger.info('Stopping file system watcher...')

    observer.join()


if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()

    vault_path = os.getenv('VAULT_PATH', './AI_Employee_Vault')
    run_filesystem_watcher(vault_path)
