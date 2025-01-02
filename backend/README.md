fileconverter/
├── pyproject.toml
├── README.md
├── fileconverter/
│   ├── __init__.py
│   ├── disk_images.py
│   ├── rom_formats.py
│   ├── archives.py
│   ├── textures.py
│   ├── audio.py
│   ├── config_files.py
│   ├── save_files.py
│   ├── compression.py
│   ├── firmware.py
│   ├── misc.py
│   └── cheats.py
└── tests/
    └── __init__.py



Here's a categorized list of file types and conversions that are relevant for videogame hacks, mods, and related use cases. This list covers common use cases in modding, emulation, and game distribution.

---

### **1. Game Disk Images**
#### File Types
- `.iso` (CD/DVD disk images)
- `.bin/.cue` (Binary disk image with a cue sheet)
- `.img` (Raw disk image)
- `.nrg` (Nero disk image)
- `.cdi` (DiscJuggler disk image)

#### Conversions
- `.iso` ↔ `.bin/.cue`
- `.iso` ↔ `.img`
- `.nrg` → `.iso`
- `.cdi` → `.iso`

---

### **2. Emulator ROM Formats**
#### File Types
- `.nes` (NES ROM)
- `.sfc` or `.smc` (SNES ROM)
- `.gba` (Game Boy Advance ROM)
- `.nds` (Nintendo DS ROM)
- `.xci` (Nintendo Switch cartridge image)
- `.nsp` (Nintendo Switch package)
- `.z64` or `.v64` (Nintendo 64 ROM)
- `.iso` or `.cso` (PlayStation Portable disk image)
- `.gcn` or `.iso` (GameCube ROM)
- `.wbfs` (Wii Backup File System)

#### Conversions
- `.iso` ↔ `.wbfs` (Wii)
- `.xci` ↔ `.nsp` (Switch)
- `.cso` ↔ `.iso` (PSP)
- `.z64` ↔ `.v64` (N64)

---

### **3. Game Archive and Mod Files**
#### File Types
- `.pak` (Unreal Engine package)
- `.wad` (Doom, Quake)
- `.bsa` (Elder Scrolls archives)
- `.dat` (Generic data file, used in many games)
- `.big` (Command & Conquer archive)
- `.vpk` (Valve package file)
- `.arc` (Various game archives)

#### Conversions
- Extract/repack:
  - `.pak` ↔ Extracted folder
  - `.wad` ↔ Extracted folder
  - `.bsa` ↔ Extracted folder
  - `.vpk` ↔ Extracted folder

---

### **4. Texture and Model Formats**
#### File Types
- `.dds` (DirectDraw Surface, textures)
- `.png` (Portable Network Graphics, textures)
- `.tga` (Targa image file, textures)
- `.obj` (Wavefront 3D model)
- `.fbx` (Autodesk 3D model)
- `.mdl` (Source Engine model)

#### Conversions
- `.dds` ↔ `.png`/`.tga`
- `.obj` ↔ `.fbx`
- `.mdl` ↔ `.obj`

---

### **5. Audio Formats**
#### File Types
- `.wav` (Waveform audio)
- `.mp3` (MPEG audio)
- `.ogg` (Ogg Vorbis, often used in games)
- `.flac` (Free Lossless Audio Codec)
- `.bnk` (WWise audio bank)

#### Conversions
- `.wav` ↔ `.mp3`/`.ogg`/`.flac`
- Extract/repack:
  - `.bnk` ↔ Extracted `.ogg` files

---

### **6. Script and Config Files**
#### File Types
- `.json` (JavaScript Object Notation)
- `.xml` (Extensible Markup Language)
- `.ini` (Initialization file, game configs)
- `.yaml` (Yet Another Markup Language)
- `.lua` (Scripting language for mods)
- `.txt` (Plain text, config or mod files)

#### Conversions
- `.json` ↔ `.xml`/`.yaml`
- `.txt` ↔ `.json` (Custom formatting for game configs)

---

### **7. Save Files**
#### File Types
- `.sav` (Generic save file)
- `.srm` (SNES save file)
- `.gci` (GameCube save file)
- `.dat` (Generic save file)
- `.bin` (Binary save data)

#### Conversions
- `.sav` ↔ Emulator-specific save formats
- `.srm` ↔ Extracted save states

---

### **8. Compression and Packaging**
#### File Types
- `.zip` (ZIP archive)
- `.rar` (RAR archive)
- `.7z` (7-Zip archive)
- `.tar.gz` (Tarball with gzip compression)

#### Conversions
- `.zip` ↔ `.7z`
- `.rar` ↔ `.zip`
- Extract/repack:
  - `.zip` ↔ Folder
  - `.rar` ↔ Folder

---

### **9. Region Locking and Firmware Formats**
#### File Types
- `.xci` (Switch cartridge)
- `.nsp` (Switch firmware)
- `.bin` (Generic binary files)

#### Conversions
- `.bin` ↔ Decrypted firmware file (specific tools required)

---

### **10. Miscellaneous Game Files**
#### File Types
- `.exe` (Windows executable)
- `.dll` (Dynamic-link library, modding hooks)
- `.py` (Python scripts for mods)
- `.apk` (Android package, mobile games)
- `.ipa` (iOS application)

#### Conversions
- Decompile/repack:
  - `.apk` ↔ Decompiled folder
  - `.ipa` ↔ Decrypted folder

---

### **11. Cheat and Trainer Files**
#### File Types
- `.ct` (Cheat Engine table)
- `.cht` (RetroArch cheat file)
- `.txt` (Plain text cheat codes)

#### Conversions
- `.txt` ↔ `.cht`