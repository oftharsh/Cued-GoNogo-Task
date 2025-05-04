# README: Cued Go/NoGo Task with EEG Recording (Muse Headset)

## Experiment Overview

This experiment investigates attention and inhibition control using a cued Go/NoGo task. This folder contains all the necessary files and resources to replicate the Cued Go/NoGo task designed for simultaneous behavioral and EEG data collection using the Muse headset. It is implemented in PsychoPy and synchronized with EEG signals collected from the Muse (MU-03) headset using LSL (Lab Streaming Layer). The task consists of 6 blocks of 100 trials each, alternating between Go (green rectangle) and NoGo (blue rectangle) stimuli, presented either horizontally or vertically. Participants respond to Go stimuli and withhold response for NoGo stimuli.

The experiment includes two within-subject sessions:
1. **Phone-Free Condition:** Participants do not use their phones during breaks.
2. **Phone-Use Condition:** Participants are free to use their phones during breaks.

## Folder & File Structure

```
├── block/                          # Contains 6 condition files (CondBlock1.xlsx–CondBlock6.xlsx)
├── data/                           # Stores CSV behavioral data and exported EEG data (from LabRecorder)
├── instructions/                   # Screens and instruction materials for participant guidance
├── Cued_GoNogo_Task.psyexp         # Main PsychoPy experiment (final, cleaned)
├── Cued_GoNogo_Task_lastrun.py     # Auto-generated script from last PsychoPy run
├── check_xdf_markers.py            # Python script to validate LSL markers in XDF files
```

## Requirements

- PsychoPy v2024.2.4
- Muse-LSL (`muselsl`)
- LabRecorder (v1.16 or higher)
- Muse headset (Model: MU-03, ID: MUSE-CD26)
- Python 3.10+ (for analysis and scripts)

## Instruction Slides
Instruction slides are located in `/instructions/` and include:
- General welcome and task overview
- Trial timeline (Go and NoGo)
- Cue-to-stimulus relationship (with arrows and visuals)
These slides can be embedded in PsychoPy or shown prior to starting the task.

## EEG & Behavioral Data

- EEG recorded at **256 Hz**, 5 channels (TP9, AF7, AF8, TP10, AUX_R).
- Behavioral data saved in CSV format for each participant.
- LSL markers include:
  - `ExperimentStart`, `Fixation`, `Cue_{Type}`, `Stimulus_{Type}`, `Response`, `Feedback_Correct_{Type}`, `Feedback_Incorrect_{Type}`, `ExperimentEnd`
  - `BreakStart_X`, `BreakEnd_X` for block transitions

## Instructions for Running

1. Launch the Muse headset and run:
  - Pair the Muse via Bluetooth.
   ```bash
   python -m muselsl stream
   ```
2. Open **LabRecorder**:
- Set the destination directory (recommended: non-OneDrive path like `D:/MuseRecordings/`)
- Ensure both `Markers` and `EEG` streams are detected.
- Start recording when ready.

3. Run the experiment from **Cued_GoNogo_Task.psyexp** in PsychoPy.
4. The `.xdf` file and `.csv` behavioral logs will be automatically saved.

## Suggested Data Analysis

- Use Python (e.g., MNE, pyxdf, pandas) or MATLAB.
- Behavioral: accuracy, mean RT, post-error slowing, signal detection metrics.
- EEG:
  - Epoching based on stimulus/response markers
  - Bandpass filter (1–40 Hz), notch filter if needed
  - Artifact rejection (e.g., amplitude thresholding)
  - Event-related potentials (ERP): especially frontocentral N2/P3

## Analyzing EEG Data (Extra)
**Check for Marker Integrity:** 
Use `check_xdf_markers.py`:
python check_xdf_markers.py
- This script loads the `.xdf` file and prints a list of all markers recorded during the experiment.

### Artifact Removal:
- Use MNE-Python:
- Apply filters (e.g., 1–30 Hz bandpass)
- Epoch around stimuli (e.g., -200 ms to 800 ms)
- Use ICA or reject based on amplitude thresholds

## Ethics & Consent

- No personal identifiers are collected.
- Informed consent required before starting.
- Participants may withdraw anytime without penalty.

## Notes for Replication
- The experiment consists of 6 blocks with 100 trials each.
- The condition files are sequentially named `CondBlock1.xlsx` to `CondBlock6.xlsx`.
- Each block includes 80% Go trials and 20% NoGo trials with randomized orientations (horizontal/vertical) and randomized cue durations.
- The experiment uses a within-subject design with participants completing two sessions:
    1. Breaks with no phone usage
    2. Breaks with phone usage
- Timing parameters (e.g., cue duration, ITI) defined in condition files

## Troubleshooting

- If PsychoPy shows `durationType` errors: ignore, they don’t affect runtime.

- LabRecorder crashes: ensure files are saved **outside OneDrive**, use D:/ or local directory.

- If markers don't show up in the XDF file:
    - Ensure `StreamInfo` name in PsychoPy is set to `"Markers"`
    - Start LabRecorder after the EEG and marker streams appear in the list

- PsychoPy crashes with `TypeError: unsupported operand type(s)`:
    - Ensure `Key_Resp.rt` is not `None` before converting to integer.
---
### Citation

If you use this experiment design or code in your research, please cite appropriately or acknowledge the original developer.
