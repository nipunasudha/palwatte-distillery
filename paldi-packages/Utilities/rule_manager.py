import pprint

ruleData = [
    {
        "variableID": "wow",
        "variableName": "wow",
        "minDangerValue": "wow",
        "minWarningValue": "wow",
        "maxWarningValue": "wow",
        "maxDangerValue": "wow"},
    {
        "variableID": "not so wow",
        "variableName": "not so wow",
        "minDangerValue": "not so wow",
        "minWarningValue": "not so wow",
        "maxWarningValue": "not so wow",
        "maxDangerValue": "not so wow"}

]


def add_rule(req):
    cmd = req.form['cmd']
    if cmd == "add":
        i1 = req.form['i1']
        i2 = req.form['i2']
        i3 = req.form['i3']
        i4 = req.form['i4']
        i5 = req.form['i5']
        ruleData.append({
            "variableID": "WW",
            "variableName": i1,
            "minDangerValue": i2,
            "minWarningValue": i3,
            "maxWarningValue": i4,
            "maxDangerValue": i5})
    pprint.pprint(cmd)
