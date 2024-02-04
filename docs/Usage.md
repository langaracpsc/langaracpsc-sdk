
LangaraCPSC (LCSC) Command Line Interface (CLI)
============

LCSC is a command-line interface tool designed to interact with the Langara CPSC API for managing execution environments (exec) and execution profiles (profile). It provides various commands to handle different operations such as creating, updating, listing, ending tenures for execution environments, and managing profiles like creation, updates, listing active profiles, and fetching specific profiles.

Installation
------------

As LCSC is a standalone Python script, no separate installation process is needed. Just make sure you have Python 3 installed on your system.

Usage
-----

To use LCSC, run the following command specifying either `exec` or `profile` followed by desired options:
```bash
lcsc [exec | profile] [options]
```
### General Options

*   Use `exec` when performing actions related to execution environments.
*   Use `profile` while working with execution profiles.

### Execution Environment (exec) Commands

#### list

Lists all available execution environments.
```bash
lcsc exec list
```
#### create

Creates new execution environments from provided JSON configuration file.
```bash
lcsc exec create <config_file.json>
```
#### update

Updates selected execution environments according to JSON configuration file.
```bash
lcsc exec update <config_file.json>
```
#### end

Terminates the tenure of specified execution environment.
```bash
lcsc exec end <exec_id>
```
### Execution Profile (profile) Commands

#### create

Generates new execution profiles via given JSON configuration file.
```bash
lcsc profile create <config_file.json>
```
#### active

Displays currently active execution profiles.
```bash
lcsc profile active
```
#### update

Modifies chosen execution profiles through JSON configuration file.
```bash
lcsc profile update <config_file.json>
```
#### <id>

Fetches details of a particular execution profile based upon its unique identifier.
```bash
lcsc profile <id>
```
Configuration
-------------

By default, LCSC looks for the configuration file named `~/.langaracpsc.json`. In case this file doesn't exist, LCSC creates an empty one. Here is the basic configuration file format:

```json
{
    "apikey": "YOUR_API_KEY",
    "baseurl": "API_BASE_URL"
}
```

Replace `YOUR_API_KEY` with actual Langara CPSC API Key and replace `API_BASE_URL` with suitable Langara CPSC API base URL.

Examples
--------

Here are some examples demonstrating common usage scenarios.

**Creating an Execution Environment:**
```bash
lcsc exec create exec_config.json
```
**Listing Active Execution Profiles:**
```bash
lcsc profile active
```
**Fetching Details of a Particular Execution Profile:**
```bash
lcsc profile 123
```
Notes
-----

Make certain that the configuration file (`~/.langaracpsc.json`) has correct settings prior to running any other commands. Also ensure proper formatting of JSON configuration files used during creating or modifying environments/profiles.