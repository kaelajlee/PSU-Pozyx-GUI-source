# PSU-Pozyx-GUI-source
A software application for interfacing with the Pozyx(R) Local Positioning
System (LPS) device from Pozyx-Labs.

## License
This software is licensed under the GNU GPL-v3-or-later free software license.
The licence is included with this software in the file `license.md`.

## Requirements
- Python 3.x
- pypozyx Python Library
- MAVEN build system
- Java SDK
- PyInstaller

## Build Instructions
- Build the python scripts into executable bundles using PyInstaller and the script `compile_python_scripts.*`
- Update `pom.xml`, if necessary
- `mvn clean`
- `mvn package`

## Authors
- Gabriel Mukobi
- Quan Ho
- Ralf Widenhorn
- Paul R. DeStefano
