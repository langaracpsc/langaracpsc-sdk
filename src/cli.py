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
        if (len(args) < 3):
            raise Exception("Insufficient arguments.")
        if (not(os.path.exists(args[2]))):
            raise Exception(f"File \"{args[2]}\" not found.")
        pass

class CLI:
    DefaultConfigPath: str = f'{os.environ["HOME"]}/.langaracpsc.json'

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

        Handlers: dict[str, CommandHandler] = {
            "exec": ExecCommandHandler()
        }

         
    def Handle(self, command: str, args: list[str]):
        self.Handlers[command].Handle(args)

CLI().Handle()

       