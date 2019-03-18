# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get(
            'https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


class ActionResponse(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_response"

    def run(self, dispatcher, tracker, domain):
        isolr_online = False
        # what your action should do
        if isolr_online:
            url = 'http://10.138.89.59:8080/iSOLR/isolrSearch'
            data = {"query": tracker.latest_message.get(
                'text'), "core": "ParseTest2"}
            isolr_response = requests.post(url, data=data)  # make an api call
            isolr_response = json.loads(isolr_response.text)
        else:
            isolr_response = {
                "responseHeader": {
                    "status": 0,
                    "QTime": 8,
                    "params": {
                        "q": "Heading2:open caveats Catalyst 9500 Series Switches OR Heading1:open caveats Catalyst 9500 Series Switches OR Content:open caveats Catalyst 9500 Series Switches",
                        "hl.useFastVectorHighlighter": "true",
                        "hl": "true",
                        "indent": "true",
                        "fl": "Heading1,Content,score",
                        "hl.fragsize": "750",
                        "hl.fl": "Heading1,Content",
                        "hl.method": "fastVector",
                        "wt": "json"
                    }
                },
                "response": {
                    "numFound": 7,
                    "start": 0,
                    "maxScore": 5.158865,
                    "docs": [
                        {
                            "Heading1": [
                                "Caveats"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 5.158865
                        },
                        {
                            "Heading1": [
                                "Caveats"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 3.8149064
                        },
                        {
                            "Heading1": [
                                "Introduction"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 2.494091
                        },
                        {
                            "Heading1": [
                                "Upgrading the Switch Software"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 1.4512058
                        },
                        {
                            "Heading1": [
                                "Upgrading the Switch Software"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 1.3581977
                        },
                        {
                            "Heading1": [
                                "Whats New in Cisco IOS XE Everest 16.6.1"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 0.7997909
                        },
                        {
                            "Heading1": [
                                "Whats New in Cisco IOS XE Everest 16.6.1"
                            ],
                            "Content": [
                                "https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/b_c9300_hig_preface_0111.html.xml&platform=Cisco%20Catalyst%209300%20Series%20Switches&release=All#bp_topic_obtaining_doc_and_submitting_request"
                            ],
                            "score": 0.7997909
                        }
                    ]
                },
                "highlighting": {
                    "cab0ce48-8c1a-4da6-80ad-2ab2db0f98d8": {
                        "Heading1": [
                            "<em>Caveats</em>"
                        ],
                        "Content": [
                            "Step 1 Ensure that you have at least 1GB of space in flash to expand a new image. Clean up old installation files in case of insufficient space. The following sample output displays the cleaning up of Cisco IOS XE Everest 16.6.1 files:\n\nUse the switch all option to clean up all the <em>switches</em> in your stack.\n\n\nNote Ignore the hexdump: messages in the CLI when you enter the command; they have no functional impact and will be removed in a later release. You will see this only on member <em>switches</em> and not on an active or standby. In the sample output below, hexdump messages are seen on switch 3, which is a member switch.\n\nSwitch# request platform software package clean switch all\nThis operation may take several minutes...\nRunning command on switch"
                        ]
                    },
                    "9032d056-a844-405c-b74d-ab4ffae77705": {
                        "Heading1": [
                            "<em>Caveats</em>"
                        ],
                        "Content": [
                            "Step 1 Ensure that you have at least 1GB of space in flash to expand a new image. Clean up old installation files in case of insufficient space.The following sample output displays the cleaning up of Cisco IOS XE Everest 16.5.1a files:\n\n\nNote Use the switch all option to clean up all the <em>switches</em> in your stack.\n\nSwitch# request platform software package clean switch all\n\nNote Ignore the hexdump: messages in the CLI when you enter the command; they have no functional impact and will be removed in a later release. You will see this only on Member <em>switches</em> and not on the active or standby. In the sample output below, hexdump messages are seen on switch 3, which is a member switch.\n\nRunning command on switch 1\nCleaning up unnecessary package"
                        ]
                    },
                    "e4184785-743a-4cdb-9c5f-bb2c7b51ece0": {
                        "Heading1": [
                            "<em>Caveats</em>"
                        ],
                        "Content": [
                            ", to a destination. The data to be streamed is driven through subscription. The feature is enabled automatically, when NETCONF-YANG is started on a device.\niPXE—An <em>open</em> Preboot eXecution Environment (PXE) client that allows a device to boot from a network boot image. iPXE is supported with IPv4 only.\nYANG Data Models—For the list of Cisco IOS XE YANG models available with this release, navigate to https://github.com/YangModels/yang/tree/master/vendor/cisco/xe/1661.\n\nRevision statements embedded in the YANG files indicate if there has been a model revision. The README.md file in the same github location highlights changes that have been made in the release.\n\nSee the Programmability Configuration Guide, Cisco IOS XE Everest 16.6.1 .\n\n(Network"
                        ]
                    },
                    "921017a5-024a-4ca2-9a92-316dcbec549b": {
                        "Heading1": [
                            "<em>Caveats</em>"
                        ],
                        "Content": [
                            ", to a destination. The data to be streamed is driven through subscription. The feature is enabled automatically, when NETCONF-YANG is started on a device.\niPXE—An <em>open</em> Preboot eXecution Environment (PXE) client that allows a device to boot from a network boot image. iPXE is supported with IPv4 only.\nYANG Data Models—For the list of Cisco IOS XE YANG models available with this release, navigate to https://github.com/YangModels/yang/tree/master/vendor/cisco/xe/1661.\n\nRevision statements embedded in the YANG files indicate if there has been a model revision. The README.md file in the same github location highlights changes that have been made in the release.\n\nSee the Programmability Configuration Guide, Cisco IOS XE Everest 16.6.1 .\n\n(Network"
                        ]
                    }
                }
            }

        response = isolr_response.get('response')
        highlighting = isolr_response.get('highlighting')

        resp = []
        docids = list(highlighting.keys())

        if isolr_response.get('responseHeader').get('status') != 0 or response.get('numFound') == 0 or len(highlighting) == 0:
            resp = "Sorry. I couldn't find related content.\nCould you please rephrase your question?"
        else:
            for i in range(3):
                resp.append('</p>' + highlighting.get(docids[i]).get('Content')[0] + '</p><a href="' + response.get('docs')[i].get('Content')[0] + '" target="_blank">See more...</a>')

        
        dispatcher.utter_attachment(resp)
        return []


