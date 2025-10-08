
# display.proto

This file details the WipperSnapper messaging API for interfacing with a display.

## WipperSnapper Components

The following WipperSnapper Components may utilize `display.proto`:

* E-Ink/E-Paper Displays
* TFT Displays
* OLED Displays
* 7-Segment Displays
* Alphanumeric Displays
* LCD Character Displays

## Sequence Diagrams

### Attaching a Display Component to a device running WipperSnapper

```mermaid
sequenceDiagram
autonumber

IO-->>Device: DisplayAddOrReplace
Note over IO, Device: DisplayType field dictates which<br>display we are using (LED, E-Ink, etc)

Device->>ws_display controller: DisplayAddOrReplace

ws_display controller->>ws_display hardware: DisplayAddOrReplace

ws_display hardware->>ws_display driver: Driver Configure Request

ws_display driver->>ws_display hardware:  Driver Configure Response

ws_display hardware->>ws_display controller: Hardware Response

ws_display controller-->>Device: DisplayAddedorReplaced

Device-->>IO: DisplayAddedorReplaced
```

### Removing a Display Component from a device running WipperSnapper

```mermaid
sequenceDiagram
autonumber

IO-->>Device: DisplayRemove
Note over IO, Device: name field dictates which<br>display we are removing

Device->>ws_display controller: DisplayRemove

ws_display controller->>ws_display hardware: Delete hardware instance

ws_display hardware->>ws_display driver: Delete driver instance

ws_display driver->>ws_display hardware: Deletion Result

ws_display hardware->>ws_display controller: Deletion Result

ws_display controller-->>Device: DisplayRemoved

Device-->>IO: DisplayRemoved
```

### Writing to a Display from IO

The display message is set by the component's feed value, which is a string. The message is sent to the display driver.

```mermaid
sequenceDiagram
autonumber

IO-->>Device: DisplayWrite
Note over IO, Device: name field dictates which<br>display we are writing to

Device->>ws_display controller: handleDisplayWrite()

ws_display controller->>ws_display hardware: Get display hardware

ws_display hardware->>ws_display driver: Execute writeX()
```