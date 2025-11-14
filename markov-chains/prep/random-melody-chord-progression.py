from mido import Message, MidiFile, MidiTrack
import random

# ---- 設定 ----
key = "C"  # 調（Cメジャー）
scale = [60, 62, 64, 65, 67, 69, 71]  # Cメジャースケール（MIDIノート番号）
chords = {
    "I":  [60, 64, 67],   # C
    "IV": [65, 69, 72],   # F
    "V":  [67, 71, 74],   # G
    "vi": [69, 72, 76]    # Am
}
progression = ["I", "V", "vi", "IV"]  # コード進行

# ---- MIDI 作成 ----
mid = MidiFile()
ch_track = MidiTrack()
mel_track = MidiTrack()
mid.tracks.append(ch_track)
mid.tracks.append(mel_track)

# ---- コード進行を配置 ----
time_per_chord = 480  # 480 ticks = 1小節相当（テンポ依存）
for chord in progression:
    notes = chords[chord]
    for note in notes:
        ch_track.append(Message('note_on', note=note, velocity=60, time=0))
    for note in notes:
        ch_track.append(Message('note_off', note=note, velocity=60, time=time_per_chord))

# ---- メロディ生成 ----
for chord in progression:
    for _ in range(4):  # 各コードに4音（8分音符想定）
        note = random.choice(scale)
        mel_track.append(Message('note_on', note=note, velocity=80, time=0))
        mel_track.append(Message('note_off', note=note, velocity=80, time=120))

# ---- 保存 ----
mid.save("auto_song.mid")
print("MIDIファイルを生成しました → auto_song.mid")