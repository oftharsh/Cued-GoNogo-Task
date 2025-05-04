import pyxdf
import matplotlib.pyplot as plt

# === LOAD THE .XDF FILE ===
file_path = r"C:\Users\Harsh\OneDrive - Jacobs University\LabRecorder_data\sub-P001\ses-S001\eeg\sub-P001_ses-S001_task-Default_run-001_eeg.xdf"
print(f"Loading: {file_path}")
streams, header = pyxdf.load_xdf(file_path)


# === LIST ALL STREAMS FOUND ===
print("\nAvailable Streams:")
for i, stream in enumerate(streams):
    print(f"{i}: {stream['info']['name'][0]}")

# === EXTRACT MARKER STREAM ===
marker_stream = None
for stream in streams:
    if stream['info']['type'][0] == 'Markers':
        marker_stream = stream
        break

if marker_stream:
    print("\n--- Markers Found ---")
    for value, timestamp in zip(marker_stream['time_series'], marker_stream['time_stamps']):
        print(f"{timestamp:.3f}s  -->  {value[0]}")
else:
    print("No marker stream found.")

# === OPTIONAL: EXTRACT MUSE EEG ===
eeg_stream = None
for stream in streams:
    if 'Muse' in stream['info']['name'][0] or stream['info']['type'][0] == 'EEG':
        eeg_stream = stream
        break

if eeg_stream:
    print("\nMuse EEG data found.")
    print(f"Shape: {eeg_stream['time_series'].shape}")
    
    # === PLOT RAW EEG (first channel only) ===
    plt.figure(figsize=(10, 4))
    plt.plot(eeg_stream['time_stamps'], [sample[0] for sample in eeg_stream['time_series']], label='EEG ch1')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (uV)')
    plt.title('Raw EEG - Channel 1')
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("No EEG stream found.")
