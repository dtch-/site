from sys import argv as args

name = args[1]

nix = {
"dtch": "detach",
"ymbx": "yumbox",
"rocx": "rocks",
"nnkd": "ninkid",
"dcat": "dead cat",
"dami": "da-me",
"nrmc": "idontknow",
"smlb": "as initials s-m-l-b",
"ttrn": "idontknow",
"mxtm": "idontknow",
"mort": "morte",
"vypr": "vyper, dumbass",
"venam": "venom, dumbass"
}

if name in nix:
    print("{} is pronounced {}".format(name,nix[name]))
