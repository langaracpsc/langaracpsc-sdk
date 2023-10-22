#!/usr/bin/env python3

import os
import sys
import json
from argparse import ArgumentParser
from langaracpscsdk.Exec import Exec, ExecManager
from langaracpscsdk.ExecImage import ExecImage, ExecImageManager
from langaracpscsdk.ExecProfile import ExecProfile, ExecProfileManager


class CommandHandler: 
    def __init__(self, command: str, usage: str = str()):
        self.Command: str = command
        self.Usage: str = usage

    def Execute(self, args: list[str]):
        pass

class ExecCommandHandler(CommandHandler):
    def __init__(self, manager: ExecManager, usage: str = str()):
        super().__init__("exec", usage)
        self.Manager: ExecManager = manager

    def Execute(self, args: list[str]):
        if (len(args) < 2):
            raise Exception(f"Insufficient arguments.\n{self.Usage}")

        command: str = args[1]

        if (command == "create"):
            if (len(args) < 3):
                raise Exception(f"Insufficient arguments.\n{self.Usage}")
            
            if (not(os.path.exists(args[2]))):
                raise Exception(f"File \"{args[2]}\" not found.")
            with open(args[2], 'r') as fp:
                execMaps: list[dict] = json.loads(fp.read())

                for execMap in execMaps:
                    created: dict = self.Manager.CreateExecDict(execMap)
                    print(f"Exec created: {created}")

        elif (command == "list"):
            for _exec in self.Manager.ListAll():
                print(_exec)

        elif (command == "update"):
            if (len(args) < 3):
                raise Exception(f"Insufficient arguments.\n{self.Usage}")
            
            if (not(os.path.exists(args[2]))):
                raise Exception(f"File \"{args[2]}\" not found.")
            with open(args[2], 'r') as fp:
                execMaps: list[dict] = json.loads(fp.read())

                for execMap in execMaps:
                    created: dict = self.Manager.UpdateExec(execMap)
                    print(f"Exec updated: {created}")

        elif (command == "end"):
            if (len(args) < 3):
                raise Exception(f"Insufficient arguments.\n{self.Usage}")

            execId: int = int(self.Manager.EndTenure(args[2]))
            print(f"Tenure ended for {execId}")
        
        else:
            raise Exception(f"Invalid command \"{args[1]}\"") 

class ExecProfileHandler(CommandHandler):
    def __init__(self, manager: ExecProfileManager, usage: str = str()):
        super().__init__("profile", usage)
        self.Manager: ExecProfileManager = manager

    def Execute(self, args: list[str]):
        if (len(args) < 2):
            raise Exception(f"Insufficient arguments.\n{self.Usage}")

        if (args[1] == "create"):
            if (len(args) < 3):
                raise Exception(f"Insufficient arguments.\n{self.Usage}")
            
            if (not(os.path.exists(args[2]))):
                raise Exception(f"File \"{args[2]}\" not found.")
            with open(args[2], 'r') as fp:
                profiles: list[dict] = json.loads(fp.read())
                try: 
                    for profile in profiles:
                        created: dict = self.Manager.CreateProfile(profile["id"], profile["image"], profile["description"])
                        print(f"Profile created: {created}")
                except KeyError as e:
                    raise Exception("Invalid field")
       
        elif (args[1] == "active"):
            for profile in self.Manager.GetActiveProfiles():
                print(profile)
        
        else:
            try:
                print(self.Manager.GetProfile(int(args[1])))
            except:
                raise Exception(f"Invalid command \"{args[1]}\"") 

class CLI:
    DefaultConfigPath: str = f'{os.environ["HOME"]}/.langaracpsc.json'

    UsageString: str = "Usage: lcsc [exec|profile]"

    @staticmethod
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

        self.ExecManagerInstance: ExecManager = ExecManager(baseUrl, apiKey)
        self.ProfileManager: ExecProfileManager = ExecProfileManager(baseUrl, f"{baseUrl}/Image", apiKey)

        self.Handlers: dict[str, CommandHandler] = {
            "exec": ExecCommandHandler(ExecManager(baseUrl, apiKey), f"Usage: lcsc exec [list | create | update | end]"),
            "profile": ExecProfileHandler(ExecProfileManager(f"{baseUrl}/Profile", f"{baseUrl}/Image", apiKey), f"Usage: lcsc profile [<id> | create | active ]")
        }

    def Handle(self, command: str, args: list[str]):
        try:
            self.Handlers[command].Execute(args)
        except KeyError:
            print(f"Invalid command.\n{CLI.UsageString}")
        except json.JSONDecodeError:
            print(f"Failed to parse JSON.")
        except BaseException as e:
            print(f"{e.args[0]}")

if (len(sys.argv) < 2):
    print(CLI.UsageString)
else:
    CLI().Handle(sys.argv[1], sys.argv[1:])