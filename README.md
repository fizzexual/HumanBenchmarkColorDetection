# Mouse Color Auto Clicker

A Python tool for automatic mouse clicks when a specific screen color appears under your cursor.

## What this does

* Tracks mouse position in real time.
* Reads pixel color under the cursor.
* Triggers a mouse click after a fixed delay.
* Runs until manual stop.

## Use cases

* UI testing
* Repetitive color based actions
* Simple automation tasks

## Requirements

* Python 3.8 or newer
* Windows, macOS, or Linux with GUI

## Dependencies

Install required libraries.

```
pip install pyautogui pillow
```

## Configuration

Edit values at the top of the script.

* TARGET_COLOR

  * RGB tuple.
  * Example: (75, 219, 106)

* CLICK_DELAY_MS

  * Delay before click.
  * Value in milliseconds.

## How to run

```
python main.py
```

## How to use

* Move your mouse over any area.
* Script checks pixel color under cursor.
* Script waits defined delay.
* Script performs mouse click.
* Press Ctrl plus C to stop.

## Notes

* Color match uses exact RGB values.
* Screen capture runs every loop cycle.
* High loop speed increases CPU usage.

## Safety

* Avoid running during normal mouse use.
* Close script before switching tasks.

## File overview

* main.py

  * Core logic.
  * Mouse tracking.
  * Color detection.
  * Click execution.

## License

MIT License
