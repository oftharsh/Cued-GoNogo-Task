# README: Cued Go/NoGo Task with EEG Recording (Muse Headset)

## Experiment Overview

This is a practice experiment that investigates attention and inhibition control using a cued Go/NoGo task. This folder contains all the necessary files and resources to replicate look and feel of the Cued Go/NoGo task designed for simultaneous behavioral and EEG data collection using the Muse headset. It is implemented in PsychoPy and synchronized with EEG signals collected from the Muse (MU-03) headset using LSL (Lab Streaming Layer). The task consists of Go (green rectangle) and NoGo (blue rectangle) stimuli, presented either horizontally or vertically. Participants respond to Go stimuli and withhold response for NoGo stimuli.

![Image](https://github.com/user-attachments/assets/8c107d40-9c03-47e6-9377-42ada6ea9af9)

## Folder & File Structure

```
├── blocks/                                  # Contains 2 condition files (CondNoGo.xlsx–CondGo.xlsx)
├── data/                                    # Stores CSV behavioral data and exported EEG data (from LabRecorder)
├── instructions/                            # Screens and instruction materials for participant guidance
├── Practice Cued_GoNogo_Task.psyexp         # Main PsychoPy experiment (final, cleaned)
├── Practice Cued_GoNogo_Task_lastrun.py     # Auto-generated script from last PsychoPy run

```

## Requirements

- PsychoPy v2024.2.4
- Muse-LSL (`muselsl`)
- LabRecorder (v1.16 or higher)
- Muse headset (Model: MU-03, ID: MUSE-CD26)
- Python 3.10+ (for analysis and scripts)

## To Replicate 
- Please go through the .readme of full experiment for detailed instructions.
---


### Citation

If you use this experiment design or code in your research, please cite appropriately or acknowledge the original developer.
