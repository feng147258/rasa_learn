#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 3:05 PM
# @Author  : Yingjun Zhu
# @File    : medical_generation.py

import json
from random import choice
# import yaml,re
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

relations = {"有...功效", "产自...地", "有...性味", "归...经", "治疗"}

with open(r"medical.json", encoding='utf-8') as rf:
    data = json.load(rf)

all_drug = set()
generation_question = [
    '请问[@](medicine)有什么功效',
    '[@](medicine)是用来干什么的',
    '请问[@](medicine)可以治疗什么',
    '请问[@](medicine)有什么疗效',
    '请问[@](medicine)是什么药',
    '请问[@](medicine)功效和作用有哪些',
    '请问[@](medicine)的效果是什么',
    '请问[@](medicine)治疗什么',
    '请问[@](medicine)治什么'
]

for drug in data:
    # print("drug : ",drug["values"])
    # print("====================")
    all_drug.add(drug["values"][0]["resourceName"])

question = []
for drug in all_drug:
    print(choice(generation_question).replace("@", drug))
    question.append(choice(generation_question).replace("@", drug))

yaml_path = r"medical_ner.yml"

data = {"nlu": {"intent": "medicals",
                "examples": question}}

for onwar in question:
    onwar = ruamel.yaml.comments.TaggedScalar('arn:aws:iam::${AWS::AccountId}:role/${GlueServiceRole}', style=None, tag=r" '[ ")

with open(yaml_path, "w", encoding="utf-8") as wf:
    yaml.dump(data, wf)
