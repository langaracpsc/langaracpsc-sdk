#!/usr/bin/env python3

import os
import sys
import json
from argparse import ArgumentParser
from langaracpscsdk import Exec
from langaracpscsdk import ExecImage
from langaracpscsdk import ExecProfile

class CommandHandler:
    def __init__(self, command: str):
        self.Command: str = command
    def Execute(self, args: list[str]):
        pass

class ExecCommandHandler(CommandHandler):
    def __init__(self, manager: Exec.ExecManager):
        super().__init__("exec")
        self.Manager: Exec.ExecManager = manager

    def Execute(self, args: list[str]):
        if (len(args) < 2):
            raise Exception("Insufficient arguments.")

        if (args[1] == "create"):
            if (not(os.path.exists(args[2]))):
                raise Exception(f"File \"{args[2]}\" not found.")
            with open(args[2], 'r') as fp:
                execMaps: list[dict] = json.loads(fp.read())

                for execMap in execMaps:
                    created: dict = self.Manager.CreateExecDict(execMap)
                    print(f"Exec created: {created}")
        
        elif (args[1] == "end"):
            execId: int = int(self.Manager.EndTenure(args[2]))
            print(f"Tenure ended for {execId}")
        
        else:
            raise Exception(f"Invalid command \"{args[1]}\"") 


class CLI:
    DefaultConfigPath: str = f'{os.environ["HOME"]}/.langaracpsc.json'

    UsageString: str = "Usage: cli [exec|profile]"

    def LoadConfig(configPath: str) -> str:
        try:
            with open(configPath, 'r') as fp:
                return json.loads(fp.read())
        except FileNotFoundError:
            print(f"Config file {configPath} doesn't exist, creating an empty config file.")
            with open(configPath, 'w') as fp:
                fp.write(json.dumps({"apikey": "", "baseurl": ""}))

        return None


    def __init__(self, configPath: str = DefaultConfigPath):
        self.Config: dict[str, str] = CLI.LoadConfig(configPath)
        
        if (self.Config == None):
            raise Exception("Failed to load the config.")
        
        baseUrl: str = self.Config["baseurl"]
        apiKey: str = self.Config["apikey"]

        self.ExecManagerInstance: Exec.ExecManager = Exec.ExecManager(baseUrl, apiKey)
        self.ProfileManager: ExecProfile.ExecProfileManager = ExecProfile.ExecProfileManager(baseUrl, f"{baseUrl}/Image", apiKey)

        self.Handlers: dict[str, CommandHandler] = {
            "exec": ExecCommandHandler(Exec.ExecManager(baseUrl, apiKey))
        }

        
    def Handle(self, command: str, args: list[str]):
        try:
            self.Handlers[command].Execute(args)
        except KeyError:
            print(f"Invalid command.\n{CLI.UsageString}")
        except json.JSONDecodeError:
            print(f"Failed to parse JSON.")
        except Exception as e:
            print(f"{e}\n{CLI.UsageString}")

if (len(sys.argv) < 2):
    print(CLI.UsageString)
else:
    CLI().Handle(sys.argv[1], sys.argv[1:])