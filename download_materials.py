"""
download_materials.py — Download all UIL academic study PDFs (2018-2026).

Directory layout:
  UIL/[Event]/[Year]/filename.pdf      (all events except CS Programming)
  UIL/Computer Science/[Year][Set]/    (CS Programming, matches existing structure)

Run: python download_materials.py
     python download_materials.py --dry-run   (print paths without downloading)
"""

import argparse
import os
import sys
import time
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

BASE = Path(__file__).parent

# ---------------------------------------------------------------------------
# All download entries: (event_folder, year, set_code_or_None, url)
# set_code is used only for "Computer Science" (Programming) to match the
# existing folder scheme  Computer Science/2023A/, 2023B/, etc.
# For every other event, files go into [Event]/[Year]/.
# ---------------------------------------------------------------------------
DOWNLOADS = [

    # ── 2018 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2018, None, "https://www.uiltexas.org/files/academics/1-Accounting_Study_Packet_InvA_2018.pdf"),
    ("Accounting", 2018, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Material_B_2018.pdf"),
    ("Accounting", 2018, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_D_2018.pdf"),
    ("Accounting", 2018, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Material_R_2018.pdf"),
    ("Accounting", 2018, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Materials_S_2018.pdf"),

    ("Calculator Applications", 2018, None, "https://www.uiltexas.org/files/academics/CalculatorApp_Study_Packet_A_2018.pdf"),
    ("Calculator Applications", 2018, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Material_B_2018.pdf"),
    ("Calculator Applications", 2018, None, "https://www.uiltexas.org/files/academics/1-Calculator_Study_Packet_D_2018.pdf"),
    ("Calculator Applications", 2018, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Materials_R_2018.pdf"),
    ("Calculator Applications", 2018, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Material_S_2018.pdf"),

    ("Computer Science Written", 2018, None, "https://www.uiltexas.org/files/academics/CompSciWritten_2018_InvA_Study_Packet.pdf"),
    ("Computer Science Written", 2018, None, "https://www.uiltexas.org/files/academics/CompSci_Study_Material_B_2018.pdf"),
    ("Computer Science Written", 2018, None, "https://www.uiltexas.org/files/academics/CompSci_2018_District_Study_Packet.pdf"),
    ("Computer Science Written", 2018, None, "https://www.uiltexas.org/files/academics/CompSci_Study_Material_R_2018.pdf"),
    ("Computer Science Written", 2018, None, "https://www.uiltexas.org/files/academics/CompSci_Study_Material_S_2018.pdf"),

    ("Copy Editing", 2018, None, "https://www.uiltexas.org/files/academics/CopyEditing_Study_Material_D_2018.pdf"),

    ("Current Issues & Events", 2018, None, "https://www.uiltexas.org/files/academics/CIE_Study_Packet_A_2018.pdf"),
    ("Current Issues & Events", 2018, None, "https://www.uiltexas.org/files/academics/CIE_Study_Material_B_2018.pdf"),
    ("Current Issues & Events", 2018, None, "https://www.uiltexas.org/files/academics/CIE_Study_Packet_D_2018.pdf"),
    ("Current Issues & Events", 2018, None, "https://www.uiltexas.org/files/academics/CIE_Study_Material_R_2018.pdf"),
    ("Current Issues & Events", 2018, None, "https://www.uiltexas.org/files/academics/CIE_Study_Material_S_2018.pdf"),

    ("Editorial Writing", 2018, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Material_A_2018.pdf"),
    ("Editorial Writing", 2018, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Material_B_2018.pdf"),
    ("Editorial Writing", 2018, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Material_D_2018.pdf"),
    ("Editorial Writing", 2018, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Material_R_2018.pdf"),
    ("Editorial Writing", 2018, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_S_18_.pdf"),

    ("Feature Writing", 2018, None, "https://www.uiltexas.org/files/academics/Feature_Study_Material_A_2018.pdf"),
    ("Feature Writing", 2018, None, "https://www.uiltexas.org/files/academics/Feature_Study_Material_B_2018.pdf"),
    ("Feature Writing", 2018, None, "https://www.uiltexas.org/files/academics/Feature_Study_Material_D_2018.pdf"),
    ("Feature Writing", 2018, None, "https://www.uiltexas.org/files/academics/Feature_Study_Material_R_2018.pdf"),
    ("Feature Writing", 2018, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_S_18_.pdf"),

    ("Headline Writing", 2018, None, "https://www.uiltexas.org/files/academics/Headline_Study_Material_A_2018.pdf"),
    ("Headline Writing", 2018, None, "https://www.uiltexas.org/files/academics/Headline_Study_Material_B_2018.pdf"),
    ("Headline Writing", 2018, None, "https://www.uiltexas.org/files/academics/Headline_Study_Material_D_2018.pdf"),
    ("Headline Writing", 2018, None, "https://www.uiltexas.org/files/academics/Headline_Study_Material_R_2018.pdf"),
    ("Headline Writing", 2018, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_S_18_.pdf"),

    ("Literary Criticism", 2018, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_Study_Material_A_2018.pdf"),
    ("Literary Criticism", 2018, None, "https://www.uiltexas.org/files/academics/LitCrit_Study_Material_B_2018.pdf"),
    ("Literary Criticism", 2018, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_Study_Material_D_2018.pdf"),
    ("Literary Criticism", 2018, None, "https://www.uiltexas.org/files/academics/LitCrit_Study_Material_R_2018.pdf"),
    ("Literary Criticism", 2018, None, "https://www.uiltexas.org/files/academics/LitCrit_Study_Material_S_2018.pdf"),

    ("Mathematics", 2018, None, "https://www.uiltexas.org/files/academics/Math_Study_Material_A_2018.pdf"),
    ("Mathematics", 2018, None, "https://www.uiltexas.org/files/academics/Math_Study_Material_B_2018.pdf"),
    ("Mathematics", 2018, None, "https://www.uiltexas.org/files/academics/Math_Study_Material_D_2018.pdf"),
    ("Mathematics", 2018, None, "https://www.uiltexas.org/files/academics/Math_Study_Material_R_2018.pdf"),
    ("Mathematics", 2018, None, "https://www.uiltexas.org/files/academics/Math_Study_Material_S_2018.pdf"),

    ("News Writing", 2018, None, "https://www.uiltexas.org/files/academics/News_Study_Material_A_2018.pdf"),
    ("News Writing", 2018, None, "https://www.uiltexas.org/files/academics/News_Study_Material_B_2018.pdf"),
    ("News Writing", 2018, None, "https://www.uiltexas.org/files/academics/News_Study_Material_D_2018.pdf"),
    ("News Writing", 2018, None, "https://www.uiltexas.org/files/academics/News_Study_Material_R_2018.pdf"),
    ("News Writing", 2018, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_S_18_.pdf"),

    ("Number Sense", 2018, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Material_A_2018.pdf"),
    ("Number Sense", 2018, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Material_B_2018.pdf"),
    ("Number Sense", 2018, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Material_D_2018.pdf"),
    ("Number Sense", 2018, None, "https://www.uiltexas.org/files/academics/Number_Sense_Study_Material_R_2018.pdf"),
    ("Number Sense", 2018, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Material_S_2018.pdf"),

    ("Ready Writing", 2018, None, "https://www.uiltexas.org/files/academics/ReadyWriting_A_18.pdf"),
    ("Ready Writing", 2018, None, "https://www.uiltexas.org/files/academics/ReadyWriting_B_2018.pdf"),
    ("Ready Writing", 2018, None, "https://www.uiltexas.org/files/academics/ReadyWriting_D_18.pdf"),
    ("Ready Writing", 2018, None, "https://www.uiltexas.org/files/academics/ReadyWriting_R_2018.pdf"),
    ("Ready Writing", 2018, None, "https://www.uiltexas.org/files/academics/ReadyWriting_S_2018.pdf"),

    ("Science", 2018, None, "https://www.uiltexas.org/files/academics/Science_Study_Material_A_2018.pdf"),
    ("Science", 2018, None, "https://www.uiltexas.org/files/academics/Science_Study_Material_B_2018.pdf"),
    ("Science", 2018, None, "https://www.uiltexas.org/files/academics/Science_Study_Material_D_2018.pdf"),
    ("Science", 2018, None, "https://www.uiltexas.org/files/academics/Science_Study_Material_R_2018.pdf"),
    ("Science", 2018, None, "https://www.uiltexas.org/files/academics/Science_Study_Material_S_2018.pdf"),

    ("Social Studies", 2018, None, "https://www.uiltexas.org/files/academics/SocialStudies_Study_Material_A_2018.pdf"),
    ("Social Studies", 2018, None, "https://www.uiltexas.org/files/academics/SocialStudies_Study_Material_B_2018.pdf"),
    ("Social Studies", 2018, None, "https://www.uiltexas.org/files/academics/SocialStudies_Study_Material_D_2018.pdf"),
    ("Social Studies", 2018, None, "https://www.uiltexas.org/files/academics/SocialStudies_Study_Materials_R_2018.pdf"),
    ("Social Studies", 2018, None, "https://www.uiltexas.org/files/academics/SocialStudies_Study_Materials_S_2018.pdf"),

    ("Spelling & Vocabulary", 2018, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Material_D_2018.pdf"),
    ("Spelling & Vocabulary", 2018, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Packet_R_2018.pdf"),
    ("Spelling & Vocabulary", 2018, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Material_S_2018.pdf"),

    # ── 2019 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2019, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_A_19.pdf"),
    ("Accounting", 2019, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_B_19.pdf"),
    ("Accounting", 2019, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_D_19.pdf"),
    ("Accounting", 2019, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_R_19.pdf"),
    ("Accounting", 2019, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_S_19.pdf"),

    ("Calculator Applications", 2019, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_A_19.pdf"),
    ("Calculator Applications", 2019, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_B_19.pdf"),
    ("Calculator Applications", 2019, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_D_19.pdf"),
    ("Calculator Applications", 2019, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_R_19.pdf"),
    ("Calculator Applications", 2019, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_S_19.pdf"),

    ("Computer Science Written", 2019, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_A_19.pdf"),
    ("Computer Science Written", 2019, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_B_19.pdf"),
    ("Computer Science Written", 2019, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_D_19.pdf"),
    ("Computer Science Written", 2019, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_R_19.pdf"),
    ("Computer Science Written", 2019, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_S_19.pdf"),

    ("Copy Editing", 2019, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_A_19.pdf"),
    ("Copy Editing", 2019, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_B_19.pdf"),
    ("Copy Editing", 2019, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_D_19.pdf"),
    ("Copy Editing", 2019, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_R_19.pdf"),
    ("Copy Editing", 2019, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_S_19.pdf"),

    ("Current Issues & Events", 2019, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_A_19.pdf"),
    ("Current Issues & Events", 2019, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_B_19.pdf"),
    ("Current Issues & Events", 2019, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_D_19.pdf"),
    ("Current Issues & Events", 2019, None, "https://www.uiltexas.org/files/academics/current_events_region__66401.pdf"),
    ("Current Issues & Events", 2019, None, "https://www.uiltexas.org/files/academics/current_events_state__26507.pdf"),

    ("Editorial Writing", 2019, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_A_19.pdf"),
    ("Editorial Writing", 2019, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_B_19.pdf"),
    ("Editorial Writing", 2019, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_D_19.pdf"),
    ("Editorial Writing", 2019, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_R_19.pdf"),
    ("Editorial Writing", 2019, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_S_19.pdf"),

    ("Feature Writing", 2019, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_A_19.pdf"),
    ("Feature Writing", 2019, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_B_19.pdf"),
    ("Feature Writing", 2019, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_D_19.pdf"),
    ("Feature Writing", 2019, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_R_19.pdf"),
    ("Feature Writing", 2019, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_S_19.pdf"),

    ("Headline Writing", 2019, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_A_19.pdf"),
    ("Headline Writing", 2019, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_B_19.pdf"),
    ("Headline Writing", 2019, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_D_19.pdf"),
    ("Headline Writing", 2019, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_R_19.pdf"),
    ("Headline Writing", 2019, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_S_19.pdf"),

    ("Literary Criticism", 2019, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_A_19.pdf"),
    ("Literary Criticism", 2019, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_B_19.pdf"),
    ("Literary Criticism", 2019, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_D_19.pdf"),
    ("Literary Criticism", 2019, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_R_19.pdf"),
    ("Literary Criticism", 2019, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_S_19.pdf"),

    ("Mathematics", 2019, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_A_19.pdf"),
    ("Mathematics", 2019, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_B_19.pdf"),
    ("Mathematics", 2019, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_D_19.pdf"),
    ("Mathematics", 2019, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_R_19.pdf"),
    ("Mathematics", 2019, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_S_19.pdf"),

    ("News Writing", 2019, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_A_19.pdf"),
    ("News Writing", 2019, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_B_19.pdf"),
    ("News Writing", 2019, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_D_19.pdf"),
    ("News Writing", 2019, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_R_19.pdf"),
    ("News Writing", 2019, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_S_19.pdf"),

    ("Number Sense", 2019, None, "https://www.uiltexas.org/files/academics/NS_StudyPacket_A_19.pdf"),
    ("Number Sense", 2019, None, "https://www.uiltexas.org/files/academics/NS_StudyPacket_B_19.pdf"),
    ("Number Sense", 2019, None, "https://www.uiltexas.org/files/academics/NS_StudyPacket_D_19.pdf"),
    ("Number Sense", 2019, None, "https://www.uiltexas.org/files/academics/NS_StudyPacket_R_19.pdf"),
    ("Number Sense", 2019, None, "https://www.uiltexas.org/files/academics/NS_StudyPacket_S_19.pdf"),

    ("Ready Writing", 2019, None, "https://www.uiltexas.org/files/academics/RW_StudyPacket_A_19.pdf"),
    ("Ready Writing", 2019, None, "https://www.uiltexas.org/files/academics/RW_StudyPacket_B_19.pdf"),
    ("Ready Writing", 2019, None, "https://www.uiltexas.org/files/academics/RW_StudyPacket_D_19.pdf"),
    ("Ready Writing", 2019, None, "https://www.uiltexas.org/files/academics/RW_StudyPacket_R_19.pdf"),
    ("Ready Writing", 2019, None, "https://www.uiltexas.org/files/academics/RW_StudyPacket_S_19.pdf"),

    ("Science", 2019, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_A_19.pdf"),
    ("Science", 2019, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_B_19.pdf"),
    ("Science", 2019, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_D_19.pdf"),
    ("Science", 2019, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_R_19.pdf"),
    ("Science", 2019, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_S_19.pdf"),

    ("Social Studies", 2019, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_A_19.pdf"),
    ("Social Studies", 2019, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_B_19.pdf"),
    ("Social Studies", 2019, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_D_19.pdf"),
    ("Social Studies", 2019, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_R_19.pdf"),
    ("Social Studies", 2019, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_S_19.pdf"),

    ("Spelling & Vocabulary", 2019, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_D_19.pdf"),
    ("Spelling & Vocabulary", 2019, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_R_19.pdf"),
    ("Spelling & Vocabulary", 2019, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_S_19.pdf"),

    # ── 2020 (COVID year — one combined packet per event, no level split) ─────
    ("Accounting", 2020, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_2020.pdf"),
    ("Calculator Applications", 2020, None, "https://www.uiltexas.org/files/academics/Calculator_Applications_Study_Packet_2020.pdf"),
    ("Computer Applications", 2020, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_2020.pdf"),
    ("Computer Science Written", 2020, None, "https://www.uiltexas.org/files/academics/Computer_Science_Written_Study_Packet_2020.pdf"),
    ("Copy Editing", 2020, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_2020.pdf"),
    ("Current Issues & Events", 2020, None, "https://www.uiltexas.org/files/academics/Current_Issues__Events_Study_Packet_2020.pdf"),
    ("Editorial Writing", 2020, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_2020.pdf"),
    ("Feature Writing", 2020, None, "https://www.uiltexas.org/files/academics/Feature_Writing_Study_Packet_2020.pdf"),
    ("Headline Writing", 2020, None, "https://www.uiltexas.org/files/academics/Headline_Writing_Study_Packet_2020.pdf"),
    ("Literary Criticism", 2020, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_2020.pdf"),
    ("Mathematics", 2020, None, "https://www.uiltexas.org/files/academics/Mathematics_Study_Packet_2020.pdf"),
    ("News Writing", 2020, None, "https://www.uiltexas.org/files/academics/News_Writing_Study_Packet_2020.pdf"),
    ("Number Sense", 2020, None, "https://www.uiltexas.org/files/academics/Number_Sense_Study_Packet_2020.pdf"),
    ("Ready Writing", 2020, None, "https://www.uiltexas.org/files/academics/Ready_Writing_Study_Packet_2020.pdf"),
    ("Science", 2020, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_2020.pdf"),
    ("Social Studies", 2020, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_2020.pdf"),
    ("Spelling & Vocabulary", 2020, None, "https://www.uiltexas.org/files/academics/Spelling__Vocabulary_Study_Packet_2020.pdf"),

    # ── 2021 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2021, None, "https://www.uiltexas.org/files/academics/Accounting_A_21.pdf"),
    ("Accounting", 2021, None, "https://www.uiltexas.org/files/academics/Accounting_B_21.pdf"),
    ("Accounting", 2021, None, "https://www.uiltexas.org/files/academics/Accounting_D_21.pdf"),
    ("Accounting", 2021, None, "https://www.uiltexas.org/files/academics/Accounting_R_21.pdf"),
    ("Accounting", 2021, None, "https://www.uiltexas.org/files/academics/Accounting_S_21.pdf"),

    ("Calculator Applications", 2021, None, "https://www.uiltexas.org/files/academics/CalcApp_A_21.pdf"),
    ("Calculator Applications", 2021, None, "https://www.uiltexas.org/files/academics/CalcApp_B_21.pdf"),
    ("Calculator Applications", 2021, None, "https://www.uiltexas.org/files/academics/Calculator_D_21.pdf"),
    ("Calculator Applications", 2021, None, "https://www.uiltexas.org/files/academics/Calculator_R_21.pdf"),
    ("Calculator Applications", 2021, None, "https://www.uiltexas.org/files/academics/Calculator_S_21.pdf"),

    ("Computer Applications", 2021, None, "https://www.uiltexas.org/files/academics/CompApp_A_21.pdf"),
    ("Computer Applications", 2021, None, "https://www.uiltexas.org/files/academics/CompApp_B_21.pdf"),
    ("Computer Applications", 2021, None, "https://www.uiltexas.org/files/academics/CompApp_D_21.pdf"),
    ("Computer Applications", 2021, None, "https://www.uiltexas.org/files/academics/CompApp_R_21.pdf"),
    ("Computer Applications", 2021, None, "https://www.uiltexas.org/files/academics/CompApp_S_21.pdf"),

    # CS Programming 2021: only ZIPs on site, no PDFs — skipped

    ("Computer Science Written", 2021, None, "https://www.uiltexas.org/files/academics/CompSciW_A_21.pdf"),
    ("Computer Science Written", 2021, None, "https://www.uiltexas.org/files/academics/CompSciW_B_21.pdf"),
    ("Computer Science Written", 2021, None, "https://www.uiltexas.org/files/academics/CompSciW_D_21.pdf"),
    ("Computer Science Written", 2021, None, "https://www.uiltexas.org/files/academics/CompSciW_R_21.pdf"),
    ("Computer Science Written", 2021, None, "https://www.uiltexas.org/files/academics/CompSciW_S_21.pdf"),

    ("Copy Editing", 2021, None, "https://www.uiltexas.org/files/academics/Copy_Editing_A_21.pdf"),
    ("Copy Editing", 2021, None, "https://www.uiltexas.org/files/academics/Copy_Editing_B_21.pdf"),
    ("Copy Editing", 2021, None, "https://www.uiltexas.org/files/academics/Copy_Editing_D_21.pdf"),
    ("Copy Editing", 2021, None, "https://www.uiltexas.org/files/academics/Copy_Editing_R_21.pdf"),
    ("Copy Editing", 2021, None, "https://www.uiltexas.org/files/academics/Copy_Editing_S_21.pdf"),

    ("Current Issues & Events", 2021, None, "https://www.uiltexas.org/files/academics/CIE_A_21.pdf"),
    ("Current Issues & Events", 2021, None, "https://www.uiltexas.org/files/academics/CIE_B_21.pdf"),
    ("Current Issues & Events", 2021, None, "https://www.uiltexas.org/files/academics/CIE_D_21.pdf"),
    ("Current Issues & Events", 2021, None, "https://www.uiltexas.org/files/academics/CIE_R_21.pdf"),
    ("Current Issues & Events", 2021, None, "https://www.uiltexas.org/files/academics/CIE_S_21.pdf"),

    ("Editorial Writing", 2021, None, "https://www.uiltexas.org/files/academics/Editorial_A_21.pdf"),
    ("Editorial Writing", 2021, None, "https://www.uiltexas.org/files/academics/Editorial_B_21.pdf"),
    ("Editorial Writing", 2021, None, "https://www.uiltexas.org/files/academics/Editorial_D_21.pdf"),
    ("Editorial Writing", 2021, None, "https://www.uiltexas.org/files/academics/Editorial_R_21.pdf"),
    ("Editorial Writing", 2021, None, "https://www.uiltexas.org/files/academics/Editorial_S_21.pdf"),

    ("Feature Writing", 2021, None, "https://www.uiltexas.org/files/academics/Feature_A_21.pdf"),
    ("Feature Writing", 2021, None, "https://www.uiltexas.org/files/academics/Feature_B_21.pdf"),
    ("Feature Writing", 2021, None, "https://www.uiltexas.org/files/academics/feature_D_21.pdf"),
    ("Feature Writing", 2021, None, "https://www.uiltexas.org/files/academics/Feature_R_21.pdf"),
    ("Feature Writing", 2021, None, "https://www.uiltexas.org/files/academics/Feature_S_21.pdf"),

    ("Headline Writing", 2021, None, "https://www.uiltexas.org/files/academics/Headline_A_21.pdf"),
    ("Headline Writing", 2021, None, "https://www.uiltexas.org/files/academics/Headline_B_21.pdf"),
    ("Headline Writing", 2021, None, "https://www.uiltexas.org/files/academics/Headline_D_21.pdf"),
    ("Headline Writing", 2021, None, "https://www.uiltexas.org/files/academics/Headline_R_21.pdf"),
    ("Headline Writing", 2021, None, "https://www.uiltexas.org/files/academics/Headline_S_21.pdf"),

    ("Literary Criticism", 2021, None, "https://www.uiltexas.org/files/academics/LitCrit_A_21.pdf"),
    ("Literary Criticism", 2021, None, "https://www.uiltexas.org/files/academics/LitCrit_B_21.pdf"),
    ("Literary Criticism", 2021, None, "https://www.uiltexas.org/files/academics/LitCrit_D_21.pdf"),
    ("Literary Criticism", 2021, None, "https://www.uiltexas.org/files/academics/LitCrit_R_21.pdf"),
    ("Literary Criticism", 2021, None, "https://www.uiltexas.org/files/academics/LitCrit_S_21.pdf"),

    ("Mathematics", 2021, None, "https://www.uiltexas.org/files/academics/Math_A_21.pdf"),
    ("Mathematics", 2021, None, "https://www.uiltexas.org/files/academics/Math_B_21.pdf"),
    ("Mathematics", 2021, None, "https://www.uiltexas.org/files/academics/Math_D_21.pdf"),
    ("Mathematics", 2021, None, "https://www.uiltexas.org/files/academics/Math_R_21.pdf"),
    ("Mathematics", 2021, None, "https://www.uiltexas.org/files/academics/Math_S_21.pdf"),

    ("News Writing", 2021, None, "https://www.uiltexas.org/files/academics/News_A_21.pdf"),
    ("News Writing", 2021, None, "https://www.uiltexas.org/files/academics/News_B_21.pdf"),
    ("News Writing", 2021, None, "https://www.uiltexas.org/files/academics/News_D_21.pdf"),
    ("News Writing", 2021, None, "https://www.uiltexas.org/files/academics/News_R_21.pdf"),
    ("News Writing", 2021, None, "https://www.uiltexas.org/files/academics/News_S_21.pdf"),

    ("Number Sense", 2021, None, "https://www.uiltexas.org/files/academics/NS_A_21.pdf"),
    ("Number Sense", 2021, None, "https://www.uiltexas.org/files/academics/NS_B_21.pdf"),
    ("Number Sense", 2021, None, "https://www.uiltexas.org/files/academics/NS_D_21.pdf"),
    ("Number Sense", 2021, None, "https://www.uiltexas.org/files/academics/NS_R_21.pdf"),
    ("Number Sense", 2021, None, "https://www.uiltexas.org/files/academics/NS_S_21.pdf"),

    ("Ready Writing", 2021, None, "https://www.uiltexas.org/files/academics/ReadyWriting_A_21.pdf"),
    ("Ready Writing", 2021, None, "https://www.uiltexas.org/files/academics/ReadyWriting_B_21.pdf"),
    ("Ready Writing", 2021, None, "https://www.uiltexas.org/files/academics/ReadyWriting_D_21.pdf"),
    ("Ready Writing", 2021, None, "https://www.uiltexas.org/files/academics/ReadyWriting_R_21.pdf"),
    ("Ready Writing", 2021, None, "https://www.uiltexas.org/files/academics/ReadyWriting_S_21.pdf"),

    ("Science", 2021, None, "https://www.uiltexas.org/files/academics/Science_A_21.pdf"),
    ("Science", 2021, None, "https://www.uiltexas.org/files/academics/Science_B_21.pdf"),
    ("Science", 2021, None, "https://www.uiltexas.org/files/academics/Science_D_21.pdf"),
    ("Science", 2021, None, "https://www.uiltexas.org/files/academics/Science_R_21.pdf"),
    ("Science", 2021, None, "https://www.uiltexas.org/files/academics/Science_S_21.pdf"),

    ("Social Studies", 2021, None, "https://www.uiltexas.org/files/academics/Social_Studies_A_21.pdf"),
    ("Social Studies", 2021, None, "https://www.uiltexas.org/files/academics/Social_Studies_B_21.pdf"),
    ("Social Studies", 2021, None, "https://www.uiltexas.org/files/academics/Social_Studies_D_21.pdf"),
    ("Social Studies", 2021, None, "https://www.uiltexas.org/files/academics/Social_Studies_R_21.pdf"),
    ("Social Studies", 2021, None, "https://www.uiltexas.org/files/academics/Social_Studies_S_21.pdf"),

    ("Spelling & Vocabulary", 2021, None, "https://www.uiltexas.org/files/academics/Spelling_D_21.pdf"),
    ("Spelling & Vocabulary", 2021, None, "https://www.uiltexas.org/files/academics/Spelling_R_21.pdf"),
    ("Spelling & Vocabulary", 2021, None, "https://www.uiltexas.org/files/academics/Spelling_S_21.pdf"),

    # ── 2022 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2022, None, "https://www.uiltexas.org/files/academics/Accounting_A_22.pdf"),
    ("Accounting", 2022, None, "https://www.uiltexas.org/files/academics/Accounting_B_22.pdf"),
    ("Accounting", 2022, None, "https://www.uiltexas.org/files/academics/Accounting_D_22.pdf"),
    ("Accounting", 2022, None, "https://www.uiltexas.org/files/academics/Accounting_R_22.pdf"),
    ("Accounting", 2022, None, "https://www.uiltexas.org/files/academics/Accounting_S_22.pdf"),

    ("Calculator Applications", 2022, None, "https://www.uiltexas.org/files/academics/Calculator_A_22.pdf"),
    ("Calculator Applications", 2022, None, "https://www.uiltexas.org/files/academics/Calculator_B_22.pdf"),
    ("Calculator Applications", 2022, None, "https://www.uiltexas.org/files/academics/Calculator_D_22.pdf"),
    ("Calculator Applications", 2022, None, "https://www.uiltexas.org/files/academics/Calculator_R_22.pdf"),
    ("Calculator Applications", 2022, None, "https://www.uiltexas.org/files/academics/Calculator_S_22.pdf"),

    ("Computer Applications", 2022, None, "https://www.uiltexas.org/files/academics/CompApp_A_22.pdf"),
    ("Computer Applications", 2022, None, "https://www.uiltexas.org/files/academics/CompApp_B_22.pdf"),
    ("Computer Applications", 2022, None, "https://www.uiltexas.org/files/academics/Computer_Applications_R_22.pdf"),
    ("Computer Applications", 2022, None, "https://www.uiltexas.org/files/academics/CompApp_S_22.pdf"),

    # CS Programming 2022: only ZIPs listed for InvA/InvB; PDF for District/Region only
    ("Computer Science", 2022, "D", "https://www.uiltexas.org/files/academics/CompSciP_D_22.pdf"),
    ("Computer Science", 2022, "R", "https://www.uiltexas.org/files/academics/CompSciP_R_22.pdf"),

    ("Computer Science Written", 2022, None, "https://www.uiltexas.org/files/academics/CompSciW_A_22.pdf"),
    ("Computer Science Written", 2022, None, "https://www.uiltexas.org/files/academics/CompSciW_B_22.pdf"),
    ("Computer Science Written", 2022, None, "https://www.uiltexas.org/files/academics/CompSciW_D_22.pdf"),
    ("Computer Science Written", 2022, None, "https://www.uiltexas.org/files/academics/CompSciW_R_22.pdf"),
    ("Computer Science Written", 2022, None, "https://www.uiltexas.org/files/academics/CompSciW_StudyPacket_S_22.pdf"),

    ("Copy Editing", 2022, None, "https://www.uiltexas.org/files/academics/Copy_Editing_A_22.pdf"),
    ("Copy Editing", 2022, None, "https://www.uiltexas.org/files/academics/Copy_Editing_B_22.pdf"),
    ("Copy Editing", 2022, None, "https://www.uiltexas.org/files/academics/Copy_Editing_D_22.pdf"),
    ("Copy Editing", 2022, None, "https://www.uiltexas.org/files/academics/Copy_Editing_R_22.pdf"),
    ("Copy Editing", 2022, None, "https://www.uiltexas.org/files/academics/Copy_Editing_S_22.pdf"),

    ("Current Issues & Events", 2022, None, "https://www.uiltexas.org/files/academics/CIE_A_22.pdf"),
    ("Current Issues & Events", 2022, None, "https://www.uiltexas.org/files/academics/CIE_B_22.pdf"),
    ("Current Issues & Events", 2022, None, "https://www.uiltexas.org/files/academics/CIE_D_22.pdf"),
    ("Current Issues & Events", 2022, None, "https://www.uiltexas.org/files/academics/CIE_R_22.pdf"),
    ("Current Issues & Events", 2022, None, "https://www.uiltexas.org/files/academics/CIE_S_22.pdf"),

    ("Editorial Writing", 2022, None, "https://www.uiltexas.org/files/academics/Editorial_A_22.pdf"),
    ("Editorial Writing", 2022, None, "https://www.uiltexas.org/files/academics/Editorial_B_22.pdf"),
    ("Editorial Writing", 2022, None, "https://www.uiltexas.org/files/academics/Editorial_D_22.pdf"),
    ("Editorial Writing", 2022, None, "https://www.uiltexas.org/files/academics/Editorial_R_22.pdf"),
    ("Editorial Writing", 2022, None, "https://www.uiltexas.org/files/academics/Editorial_S_22.pdf"),

    ("Feature Writing", 2022, None, "https://www.uiltexas.org/files/academics/Feature_A_22.pdf"),
    ("Feature Writing", 2022, None, "https://www.uiltexas.org/files/academics/Feature_B_22.pdf"),
    ("Feature Writing", 2022, None, "https://www.uiltexas.org/files/academics/Feature_D_22.pdf"),
    ("Feature Writing", 2022, None, "https://www.uiltexas.org/files/academics/Feature_R_22.pdf"),
    ("Feature Writing", 2022, None, "https://www.uiltexas.org/files/academics/Feature_S_22.pdf"),

    ("Headline Writing", 2022, None, "https://www.uiltexas.org/files/academics/Headline_A_22.pdf"),
    ("Headline Writing", 2022, None, "https://www.uiltexas.org/files/academics/Headline_B_22.pdf"),
    ("Headline Writing", 2022, None, "https://www.uiltexas.org/files/academics/Headline_D_22.pdf"),
    ("Headline Writing", 2022, None, "https://www.uiltexas.org/files/academics/Headline_R_22.pdf"),
    ("Headline Writing", 2022, None, "https://www.uiltexas.org/files/academics/Headline_S_22.pdf"),

    ("Literary Criticism", 2022, None, "https://www.uiltexas.org/files/academics/LitCrit_A_22.pdf"),
    ("Literary Criticism", 2022, None, "https://www.uiltexas.org/files/academics/LitCrit_B_22.pdf"),
    ("Literary Criticism", 2022, None, "https://www.uiltexas.org/files/academics/LitCrit_D_22.pdf"),
    ("Literary Criticism", 2022, None, "https://www.uiltexas.org/files/academics/LitCrit_R_22.pdf"),
    ("Literary Criticism", 2022, None, "https://www.uiltexas.org/files/academics/LitCrit_S_22.pdf"),

    ("Mathematics", 2022, None, "https://www.uiltexas.org/files/academics/Math_A_22.pdf"),
    ("Mathematics", 2022, None, "https://www.uiltexas.org/files/academics/Math_B_22.pdf"),
    ("Mathematics", 2022, None, "https://www.uiltexas.org/files/academics/Math_D_22.pdf"),
    ("Mathematics", 2022, None, "https://www.uiltexas.org/files/academics/Math__R_22.pdf"),
    ("Mathematics", 2022, None, "https://www.uiltexas.org/files/academics/Math_S_22.pdf"),

    ("News Writing", 2022, None, "https://www.uiltexas.org/files/academics/News_A_22.pdf"),
    ("News Writing", 2022, None, "https://www.uiltexas.org/files/academics/News_B_22.pdf"),
    ("News Writing", 2022, None, "https://www.uiltexas.org/files/academics/News_D_22.pdf"),
    ("News Writing", 2022, None, "https://www.uiltexas.org/files/academics/News_R_22.pdf"),
    ("News Writing", 2022, None, "https://www.uiltexas.org/files/academics/News_S_22.pdf"),

    ("Number Sense", 2022, None, "https://www.uiltexas.org/files/academics/NS_A_22.pdf"),
    ("Number Sense", 2022, None, "https://www.uiltexas.org/files/academics/NS_B_22.pdf"),
    ("Number Sense", 2022, None, "https://www.uiltexas.org/files/academics/NS_D_22.pdf"),
    ("Number Sense", 2022, None, "https://www.uiltexas.org/files/academics/NumberSense_R_22.pdf"),
    ("Number Sense", 2022, None, "https://www.uiltexas.org/files/academics/NS_S_22.pdf"),

    ("Ready Writing", 2022, None, "https://www.uiltexas.org/files/academics/ReadyWriting_A_22.pdf"),
    ("Ready Writing", 2022, None, "https://www.uiltexas.org/files/academics/ReadyWriting_B_22.pdf"),
    ("Ready Writing", 2022, None, "https://www.uiltexas.org/files/academics/ReadyWriting_D_22.pdf"),
    ("Ready Writing", 2022, None, "https://www.uiltexas.org/files/academics/ReadyWriting_R_22.pdf"),
    ("Ready Writing", 2022, None, "https://www.uiltexas.org/files/academics/ReadyWriting_S_22.pdf"),

    ("Science", 2022, None, "https://www.uiltexas.org/files/academics/Science_A_22.pdf"),
    ("Science", 2022, None, "https://www.uiltexas.org/files/academics/Science_B_22.pdf"),
    ("Science", 2022, None, "https://www.uiltexas.org/files/academics/Science_D_22.pdf"),
    ("Science", 2022, None, "https://www.uiltexas.org/files/academics/Science_R_22.pdf"),
    ("Science", 2022, None, "https://www.uiltexas.org/files/academics/Science_S_22.pdf"),

    ("Social Studies", 2022, None, "https://www.uiltexas.org/files/academics/Social_Studies_A_22.pdf"),
    ("Social Studies", 2022, None, "https://www.uiltexas.org/files/academics/Social_Studies_B_22.pdf"),
    ("Social Studies", 2022, None, "https://www.uiltexas.org/files/academics/Social_Studies_D_22.pdf"),
    ("Social Studies", 2022, None, "https://www.uiltexas.org/files/academics/SocialStudies_R_22.pdf"),
    ("Social Studies", 2022, None, "https://www.uiltexas.org/files/academics/SocialStudies_S_22.pdf"),

    ("Spelling & Vocabulary", 2022, None, "https://www.uiltexas.org/files/academics/Spelling_D_22.pdf"),
    ("Spelling & Vocabulary", 2022, None, "https://www.uiltexas.org/files/academics/Spelling_R_22.pdf"),
    ("Spelling & Vocabulary", 2022, None, "https://www.uiltexas.org/files/academics/Spelling_S_22.pdf"),

    # ── 2023 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2023, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_A_23.pdf"),
    ("Accounting", 2023, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_B_23.pdf"),
    ("Accounting", 2023, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_D_23.pdf"),
    ("Accounting", 2023, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_R_23.pdf"),
    ("Accounting", 2023, None, "https://www.uiltexas.org/files/academics/Accounting_Study_Packet_S_23.pdf"),

    ("Calculator Applications", 2023, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Packet_A_23.pdf"),
    ("Calculator Applications", 2023, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Packet_B_23.pdf"),
    ("Calculator Applications", 2023, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Packet_D_23.pdf"),
    ("Calculator Applications", 2023, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Packet_R_23.pdf"),
    ("Calculator Applications", 2023, None, "https://www.uiltexas.org/files/academics/Calculator_Study_Packet_S_23.pdf"),

    ("Computer Applications", 2023, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_A_23.pdf"),
    ("Computer Applications", 2023, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_B_23.pdf"),
    ("Computer Applications", 2023, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_D_23.pdf"),
    ("Computer Applications", 2023, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_R_23.pdf"),
    ("Computer Applications", 2023, None, "https://www.uiltexas.org/files/academics/Computer_Applications_Study_Packet_S_23.pdf"),

    # CS Programming 2023 — PDFs go into Computer Science/[Year][Set]/
    ("Computer Science", 2023, "A", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_A_23.pdf"),
    ("Computer Science", 2023, "B", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_B_23.pdf"),
    ("Computer Science", 2023, "D", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_D_23.pdf"),
    ("Computer Science", 2023, "R", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_R_23.pdf"),
    ("Computer Science", 2023, "S", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_S_23.pdf"),

    ("Computer Science Written", 2023, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_A_23.pdf"),
    ("Computer Science Written", 2023, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_B_23.pdf"),
    ("Computer Science Written", 2023, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_D_23.pdf"),
    ("Computer Science Written", 2023, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_R_23.pdf"),
    ("Computer Science Written", 2023, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_S_23.pdf"),

    ("Copy Editing", 2023, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_A_23.pdf"),
    ("Copy Editing", 2023, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_B_23.pdf"),
    ("Copy Editing", 2023, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_D_23.pdf"),
    ("Copy Editing", 2023, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_R_23.pdf"),
    ("Copy Editing", 2023, None, "https://www.uiltexas.org/files/academics/Copy_Editing_Study_Packet_S_23.pdf"),

    ("Current Issues & Events", 2023, None, "https://www.uiltexas.org/files/academics/Current_Issues_Study_Packet_A_23.pdf"),
    ("Current Issues & Events", 2023, None, "https://www.uiltexas.org/files/academics/Current_Issues_Study_Packet_B_23.pdf"),
    ("Current Issues & Events", 2023, None, "https://www.uiltexas.org/files/academics/Current_Issues_Study_Packet_D_23.pdf"),
    ("Current Issues & Events", 2023, None, "https://www.uiltexas.org/files/academics/Current_Issues_Study_Packet_R_23.pdf"),
    ("Current Issues & Events", 2023, None, "https://www.uiltexas.org/files/academics/Current_Issues_Study_Packet_S_23.pdf"),

    ("Editorial Writing", 2023, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_A_23.pdf"),
    ("Editorial Writing", 2023, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_B_23.pdf"),
    ("Editorial Writing", 2023, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_D_23.pdf"),
    ("Editorial Writing", 2023, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_R_23.pdf"),
    ("Editorial Writing", 2023, None, "https://www.uiltexas.org/files/academics/Editorial_Study_Packet_S_23.pdf"),

    ("Feature Writing", 2023, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_A_23.pdf"),
    ("Feature Writing", 2023, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_B_23.pdf"),
    ("Feature Writing", 2023, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_D_23.pdf"),
    ("Feature Writing", 2023, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_R_23.pdf"),
    ("Feature Writing", 2023, None, "https://www.uiltexas.org/files/academics/Feature_Study_Packet_S_23.pdf"),

    ("Headline Writing", 2023, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_A_23.pdf"),
    ("Headline Writing", 2023, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_B_23.pdf"),
    ("Headline Writing", 2023, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_D_23.pdf"),
    ("Headline Writing", 2023, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_R_23.pdf"),
    ("Headline Writing", 2023, None, "https://www.uiltexas.org/files/academics/Headline_Study_Packet_S_23.pdf"),

    ("Literary Criticism", 2023, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_A_23.pdf"),
    ("Literary Criticism", 2023, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_B_23.pdf"),
    ("Literary Criticism", 2023, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_D_23.pdf"),
    ("Literary Criticism", 2023, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_R_23.pdf"),
    ("Literary Criticism", 2023, None, "https://www.uiltexas.org/files/academics/Literary_Criticism_Study_Packet_S_23.pdf"),

    ("Mathematics", 2023, None, "https://www.uiltexas.org/files/academics/Math_Study_Packet_A_23.pdf"),
    ("Mathematics", 2023, None, "https://www.uiltexas.org/files/academics/Math_Study_Packet_B_23.pdf"),
    ("Mathematics", 2023, None, "https://www.uiltexas.org/files/academics/Math_Study_Packet_D_23.pdf"),
    ("Mathematics", 2023, None, "https://www.uiltexas.org/files/academics/Math_Study_Packet_R_23.pdf"),
    ("Mathematics", 2023, None, "https://www.uiltexas.org/files/academics/Math_Study_Packet_S_23.pdf"),

    ("News Writing", 2023, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_A_23.pdf"),
    ("News Writing", 2023, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_B_23.pdf"),
    ("News Writing", 2023, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_D_23.pdf"),
    ("News Writing", 2023, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_R_23.pdf"),
    ("News Writing", 2023, None, "https://www.uiltexas.org/files/academics/News_Study_Packet_S_23.pdf"),

    ("Number Sense", 2023, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Packet_A_23.pdf"),
    ("Number Sense", 2023, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Packet_B_23..pdf"),
    ("Number Sense", 2023, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Packet_D_23.pdf"),
    ("Number Sense", 2023, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Packet_R_23.pdf"),
    ("Number Sense", 2023, None, "https://www.uiltexas.org/files/academics/NumberSense_Study_Packet_S_23.pdf"),

    ("Ready Writing", 2023, None, "https://www.uiltexas.org/files/academics/ReadyWriting_A_23.pdf"),
    ("Ready Writing", 2023, None, "https://www.uiltexas.org/files/academics/ReadyWriting_B_23.pdf"),
    ("Ready Writing", 2023, None, "https://www.uiltexas.org/files/academics/ReadyWriting_D_23.pdf"),
    ("Ready Writing", 2023, None, "https://www.uiltexas.org/files/academics/ReadyWriting_R_23.pdf"),
    ("Ready Writing", 2023, None, "https://www.uiltexas.org/files/academics/ReadyWriting_S_23.pdf"),

    ("Science", 2023, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_A_23.pdf"),
    ("Science", 2023, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_B_23.pdf"),
    ("Science", 2023, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_D_23.pdf"),
    ("Science", 2023, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_R_23.pdf"),
    ("Science", 2023, None, "https://www.uiltexas.org/files/academics/Science_Study_Packet_S_23.pdf"),

    ("Social Studies", 2023, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_A_23.pdf"),
    ("Social Studies", 2023, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_B_23.pdf"),
    ("Social Studies", 2023, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_D_23.pdf"),
    ("Social Studies", 2023, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_R_23.pdf"),
    ("Social Studies", 2023, None, "https://www.uiltexas.org/files/academics/Social_Studies_Study_Packet_S_23.pdf"),

    ("Spelling & Vocabulary", 2023, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Packet_D_23.pdf"),
    ("Spelling & Vocabulary", 2023, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Packet_R_23.pdf"),
    ("Spelling & Vocabulary", 2023, None, "https://www.uiltexas.org/files/academics/Spelling_Study_Packet_S_23.pdf"),

    # ── 2024 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2024, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_A_24.pdf"),
    ("Accounting", 2024, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_B_24.pdf"),
    ("Accounting", 2024, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_D_24.pdf"),
    ("Accounting", 2024, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_R_24.pdf"),
    ("Accounting", 2024, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_S_24.pdf"),

    ("Calculator Applications", 2024, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_A_24.pdf"),
    ("Calculator Applications", 2024, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_B_24.pdf"),
    ("Calculator Applications", 2024, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_D_24.pdf"),
    ("Calculator Applications", 2024, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_R_24.pdf"),
    ("Calculator Applications", 2024, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_S_24.pdf"),

    ("Computer Applications", 2024, None, "https://www.uiltexas.org/files/academics/CompApp_StudyPacket_A_24.pdf"),
    ("Computer Applications", 2024, None, "https://www.uiltexas.org/files/academics/CompApp_StudyPacket_B_24.pdf"),
    ("Computer Applications", 2024, None, "https://www.uiltexas.org/files/academics/CompApp_StudyPacket_D_24.pdf"),
    ("Computer Applications", 2024, None, "https://www.uiltexas.org/files/academics/CompApp_StudyPacket_R_24.pdf"),
    ("Computer Applications", 2024, None, "https://www.uiltexas.org/files/academics/CompApp_StudyPacket_S_24.pdf"),

    # CS Programming 2024 — already partially on disk; still download PDFs
    ("Computer Science", 2024, "A", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_A_24.pdf"),
    ("Computer Science", 2024, "B", "https://www.uiltexas.org/files/academics/CompSciP_Study_Packet_B_24.pdf"),
    ("Computer Science", 2024, "D", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_D_24.pdf"),
    ("Computer Science", 2024, "R", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_R_24.pdf"),
    ("Computer Science", 2024, "S", "https://www.uiltexas.org/files/academics/CompSciProg_StudyPacket_S-2024.pdf"),

    ("Computer Science Written", 2024, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_A_24.pdf"),
    ("Computer Science Written", 2024, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_B_24.pdf"),
    ("Computer Science Written", 2024, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_D_24.pdf"),
    ("Computer Science Written", 2024, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_R_24.pdf"),
    ("Computer Science Written", 2024, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_S_2024.pdf"),

    ("Copy Editing", 2024, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_A_24.pdf"),
    ("Copy Editing", 2024, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_B_24.pdf"),
    ("Copy Editing", 2024, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_D__24.pdf"),
    ("Copy Editing", 2024, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_R_24.pdf"),
    ("Copy Editing", 2024, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_S__24.pdf"),

    ("Current Issues & Events", 2024, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_A_24.pdf"),
    ("Current Issues & Events", 2024, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_B_24.pdf"),
    ("Current Issues & Events", 2024, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_D_24.pdf"),
    ("Current Issues & Events", 2024, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_R_24.pdf"),
    ("Current Issues & Events", 2024, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_S_24.pdf"),

    ("Editorial Writing", 2024, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_A_24.pdf"),
    ("Editorial Writing", 2024, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_B_24.pdf"),
    ("Editorial Writing", 2024, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_D_24.pdf"),
    ("Editorial Writing", 2024, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_R_24.pdf"),
    ("Editorial Writing", 2024, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_S_24.pdf"),

    ("Feature Writing", 2024, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_A_24.pdf"),
    ("Feature Writing", 2024, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_B_24.pdf"),
    ("Feature Writing", 2024, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_D_24.pdf"),
    ("Feature Writing", 2024, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_R_24.pdf"),
    ("Feature Writing", 2024, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_S_24.pdf"),

    ("Headline Writing", 2024, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_A_24.pdf"),
    ("Headline Writing", 2024, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_B_24.pdf"),
    ("Headline Writing", 2024, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_D_24.pdf"),
    ("Headline Writing", 2024, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_R_24.pdf"),
    ("Headline Writing", 2024, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_S_24.pdf"),

    ("Literary Criticism", 2024, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_StudyPacket_A_24.pdf"),
    ("Literary Criticism", 2024, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_StudyPacket_B_24.pdf"),
    ("Literary Criticism", 2024, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_StudyPacket_D_24.pdf"),
    ("Literary Criticism", 2024, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_StudyPacket_R_24.pdf"),
    ("Literary Criticism", 2024, None, "https://www.uiltexas.org/files/academics/LiteraryCriticism_StudyPacket_S_24.pdf"),

    ("Mathematics", 2024, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_A_24.pdf"),
    ("Mathematics", 2024, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_B_24.pdf"),
    ("Mathematics", 2024, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_D_24.pdf"),
    ("Mathematics", 2024, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_R_24.pdf"),
    ("Mathematics", 2024, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_S_24.pdf"),

    ("News Writing", 2024, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_A_24.pdf"),
    ("News Writing", 2024, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_B_24.pdf"),
    ("News Writing", 2024, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_D_2024.pdf"),
    ("News Writing", 2024, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_R_24.pdf"),
    ("News Writing", 2024, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_S_24.pdf"),

    ("Number Sense", 2024, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_A_24.pdf"),
    ("Number Sense", 2024, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_B_24.pdf"),
    ("Number Sense", 2024, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_D_24.pdf"),
    ("Number Sense", 2024, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_R_24.pdf"),
    ("Number Sense", 2024, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_S_24.pdf"),

    ("Ready Writing", 2024, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_A_24.pdf"),
    ("Ready Writing", 2024, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_B_24.pdf"),
    ("Ready Writing", 2024, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_D_24.pdf"),
    ("Ready Writing", 2024, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_R_24.pdf"),
    ("Ready Writing", 2024, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_S_24.pdf"),

    ("Science", 2024, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_A_24.pdf"),
    ("Science", 2024, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_B_24.pdf"),
    ("Science", 2024, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_D_24.pdf"),
    ("Science", 2024, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_R_24.pdf"),
    ("Science", 2024, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_S_24.pdf"),

    ("Social Studies", 2024, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_A_24.pdf"),
    ("Social Studies", 2024, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_B_24.pdf"),
    ("Social Studies", 2024, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_D_24.pdf"),
    ("Social Studies", 2024, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_R_24.pdf"),
    ("Social Studies", 2024, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_S_24.pdf"),

    ("Spelling & Vocabulary", 2024, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_D_24.pdf"),
    ("Spelling & Vocabulary", 2024, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_R_24.pdf"),
    ("Spelling & Vocabulary", 2024, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_S_24.pdf"),

    # ── 2025 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2025, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_A_25.pdf"),
    ("Accounting", 2025, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_B_25.pdf"),
    ("Accounting", 2025, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_D_25.pdf"),
    ("Accounting", 2025, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_R_25.pdf"),
    ("Accounting", 2025, None, "https://www.uiltexas.org/files/academics/Accounting_StudyPacket_S_25.pdf"),

    ("Calculator Applications", 2025, None, "https://www.uiltexas.org/files/academics/CalculatorApp_StudyPacket_A_25.pdf"),
    ("Calculator Applications", 2025, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_B_25.pdf"),
    ("Calculator Applications", 2025, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_D_25.pdf"),
    ("Calculator Applications", 2025, None, "https://www.uiltexas.org/files/academics/Calculator_StudyPacket_R_25.pdf"),
    ("Calculator Applications", 2025, None, "https://www.uiltexas.org/files/academics/CalcApp_StudyPacket_S_25.pdf"),

    # CS Programming 2025
    ("Computer Science", 2025, "A", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_A_25.pdf"),
    ("Computer Science", 2025, "B", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_B_25.pdf"),
    ("Computer Science", 2025, "D", "https://www.uiltexas.org/files/academics/CompSciP_StudyPacket_D_25pdf.pdf"),
    ("Computer Science", 2025, "R", "https://www.uiltexas.org/files/academics/UILCS_Region_2025_Student_Packet.pdf"),

    ("Computer Science Written", 2025, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_A_25.pdf"),
    ("Computer Science Written", 2025, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_B_25.pdf"),
    ("Computer Science Written", 2025, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_D_25.pdf"),
    ("Computer Science Written", 2025, None, "https://www.uiltexas.org/files/academics/CompSciWritten_StudyPacket_R_25.pdf"),
    ("Computer Science Written", 2025, None, "https://www.uiltexas.org/files/academics/CompSci_StudyPacket_S_25.pdf"),

    ("Copy Editing", 2025, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_A_25.pdf"),
    ("Copy Editing", 2025, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_B_25.pdf"),
    ("Copy Editing", 2025, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_D_2025.pdf"),
    ("Copy Editing", 2025, None, "https://www.uiltexas.org/files/academics/CopyEditing_StudyPacket_R_25.pdf"),
    ("Copy Editing", 2025, None, "https://www.uiltexas.org/files/academics/CE_State_2025.pdf"),

    ("Current Issues & Events", 2025, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_A_25.pdf"),
    ("Current Issues & Events", 2025, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_B_25.pdf"),
    ("Current Issues & Events", 2025, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_D_25.pdf"),
    ("Current Issues & Events", 2025, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_R_25.pdf"),
    ("Current Issues & Events", 2025, None, "https://www.uiltexas.org/files/academics/CIE_StudyPacket_S_25.pdf"),

    ("Editorial Writing", 2025, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_A_25.pdf"),
    ("Editorial Writing", 2025, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_B_25.pdf"),
    ("Editorial Writing", 2025, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_D_2025.pdf"),
    ("Editorial Writing", 2025, None, "https://www.uiltexas.org/files/academics/Editorial_StudyPacket_R_25.pdf"),
    ("Editorial Writing", 2025, None, "https://www.uiltexas.org/files/academics/EW_State_2025.pdf"),

    ("Feature Writing", 2025, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_A_25.pdf"),
    ("Feature Writing", 2025, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_B_25.pdf"),
    ("Feature Writing", 2025, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_D_2025.pdf"),
    ("Feature Writing", 2025, None, "https://www.uiltexas.org/files/academics/Feature_StudyPacket_R_25.pdf"),
    ("Feature Writing", 2025, None, "https://www.uiltexas.org/files/academics/FW_State_2025.pdf"),

    ("Headline Writing", 2025, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_A_25.pdf"),
    ("Headline Writing", 2025, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_B_25.pdf"),
    ("Headline Writing", 2025, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_D_2025.pdf"),
    ("Headline Writing", 2025, None, "https://www.uiltexas.org/files/academics/Headline_StudyPacket_R_25.pdf"),
    ("Headline Writing", 2025, None, "https://www.uiltexas.org/files/academics/HW_State_2025.pdf"),

    ("Literary Criticism", 2025, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_A_25.pdf"),
    ("Literary Criticism", 2025, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_B_25.pdf"),
    ("Literary Criticism", 2025, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_D_25.pdf"),
    ("Literary Criticism", 2025, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_R_25.pdf"),
    ("Literary Criticism", 2025, None, "https://www.uiltexas.org/files/academics/LitCrit_StudyPacket_S_25.pdf"),

    ("Mathematics", 2025, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_A_25.pdf"),
    ("Mathematics", 2025, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_B_25.pdf"),
    ("Mathematics", 2025, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_D_25.pdf"),
    ("Mathematics", 2025, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_R_25.pdf"),
    ("Mathematics", 2025, None, "https://www.uiltexas.org/files/academics/Math_StudyPacket_S_25.pdf"),

    ("News Writing", 2025, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_A_25.pdf"),
    ("News Writing", 2025, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_B_25.pdf"),
    ("News Writing", 2025, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_D_2025.pdf"),
    ("News Writing", 2025, None, "https://www.uiltexas.org/files/academics/News_StudyPacket_R_25.pdf"),
    ("News Writing", 2025, None, "https://www.uiltexas.org/files/academics/NW_State_2025.pdf"),

    ("Number Sense", 2025, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_A_25.pdf"),
    ("Number Sense", 2025, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_B_25.pdf"),
    ("Number Sense", 2025, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_D_25.pdf"),
    ("Number Sense", 2025, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_R_25.pdf"),
    ("Number Sense", 2025, None, "https://www.uiltexas.org/files/academics/NumberSense_StudyPacket_S_25.pdf"),

    ("Ready Writing", 2025, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_A_25.pdf"),
    ("Ready Writing", 2025, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_B_25.pdf"),
    ("Ready Writing", 2025, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_D_25.pdf"),
    ("Ready Writing", 2025, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_R_25.pdf"),
    ("Ready Writing", 2025, None, "https://www.uiltexas.org/files/academics/ReadyWriting_StudyPacket_S_25.pdf"),

    ("Science", 2025, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_A_25.pdf"),
    ("Science", 2025, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_B_25.pdf"),
    ("Science", 2025, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_D_25.pdf"),
    ("Science", 2025, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_R_25.pdf"),
    ("Science", 2025, None, "https://www.uiltexas.org/files/academics/Science_StudyPacket_S_25.pdf"),

    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/Social_Studies_STUDY_GUIDE_2025-26_updated.pdf"),
    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_A_25.pdf"),
    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_B_25.pdf"),
    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_D_25.pdf"),
    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/SocialStudies_StudyPacket_R_25.pdf"),
    ("Social Studies", 2025, None, "https://www.uiltexas.org/files/academics/Social_Studies_StudyPacket_S_25.pdf"),

    ("Spelling & Vocabulary", 2025, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_D_25.pdf"),
    ("Spelling & Vocabulary", 2025, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_R_25.pdf"),
    ("Spelling & Vocabulary", 2025, None, "https://www.uiltexas.org/files/academics/Spelling_StudyPacket_S_25.pdf"),

    # ── 2026 ─────────────────────────────────────────────────────────────────
    ("Accounting", 2026, None, "https://www.uiltexas.org/files/academics/Accounting_SM_A_26.pdf"),
    ("Accounting", 2026, None, "https://www.uiltexas.org/files/academics/Accounting_SM_B_26.pdf"),
    ("Accounting", 2026, None, "https://www.uiltexas.org/files/academics/Accounting_SM_D_26.pdf"),

    ("Calculator Applications", 2026, None, "https://www.uiltexas.org/files/academics/Calculator_SM_A_26.pdf"),
    ("Calculator Applications", 2026, None, "https://www.uiltexas.org/files/academics/Calculator_SM_B_26.pdf"),
    ("Calculator Applications", 2026, None, "https://www.uiltexas.org/files/academics/Calculator_SM_D_26.pdf"),

    # CS Programming 2026
    ("Computer Science", 2026, "A", "https://www.uiltexas.org/files/academics/CompSci_InvA_2026_Student_Packet_SM.pdf"),
    ("Computer Science", 2026, "B", "https://www.uiltexas.org/files/academics/CS_InvB_2026_Student_Packet_SM.pdf"),
    ("Computer Science", 2026, "D", "https://www.uiltexas.org/files/academics/CompSci_Programming_Student_SM_D_26_.pdf"),

    ("Computer Science Written", 2026, None, "https://www.uiltexas.org/files/academics/CompSci_WrittenTest_SM_A_26.pdf"),
    ("Computer Science Written", 2026, None, "https://www.uiltexas.org/files/academics/CompSci_WrittenTest_SM_B_26.pdf"),
    ("Computer Science Written", 2026, None, "https://www.uiltexas.org/files/academics/CompSci_Written_SM_D_26.pdf"),

    ("Copy Editing", 2026, None, "https://www.uiltexas.org/files/academics/CopyEditing_Contest_InvA_2026_SM.pdf"),
    ("Copy Editing", 2026, None, "https://www.uiltexas.org/files/academics/CopyEditing_Contest_InvB_2026-REV2-12_SM.pdf"),
    ("Copy Editing", 2026, None, "https://www.uiltexas.org/files/academics/CopyEditing_SM_District_2026.pdf"),

    ("Current Issues & Events", 2026, None, "https://www.uiltexas.org/files/academics/CIE_SM_A_26.pdf"),
    ("Current Issues & Events", 2026, None, "https://www.uiltexas.org/files/academics/CIE_SM_B_26.pdf"),
    ("Current Issues & Events", 2026, None, "https://www.uiltexas.org/files/academics/CIE_SM_D_26-Rev2-23v2.pdf"),

    ("Editorial Writing", 2026, None, "https://www.uiltexas.org/files/academics/Editorial_Contest_InvA_2026_SM.pdf"),
    ("Editorial Writing", 2026, None, "https://www.uiltexas.org/files/academics/Editorial_Contest_InvB_2026_SM.pdf"),
    ("Editorial Writing", 2026, None, "https://www.uiltexas.org/files/academics/Editorial_SM_District_2026.pdf"),

    ("Feature Writing", 2026, None, "https://www.uiltexas.org/files/academics/Feature_Contest_InvA_2026_SM.pdf"),
    ("Feature Writing", 2026, None, "https://www.uiltexas.org/files/academics/Feature_Contest_InvB_2026_SM.pdf"),
    ("Feature Writing", 2026, None, "https://www.uiltexas.org/files/academics/Feature_SM_District_2026-Rev2-2.pdf"),

    ("Headline Writing", 2026, None, "https://www.uiltexas.org/files/academics/Headline_Contest_InvA_2026_SM.pdf"),
    ("Headline Writing", 2026, None, "https://www.uiltexas.org/files/academics/Headline_Contest_InvB_2026_SM.pdf"),
    ("Headline Writing", 2026, None, "https://www.uiltexas.org/files/academics/Headline_SM_District_2026.pdf"),

    ("Literary Criticism", 2026, None, "https://www.uiltexas.org/files/academics/LitCrit_SM_A_26_Rev1-20.pdf"),
    ("Literary Criticism", 2026, None, "https://www.uiltexas.org/files/academics/LitCrit_SM_B_26.pdf"),
    ("Literary Criticism", 2026, None, "https://www.uiltexas.org/files/academics/LitCrit_SM_D_26.pdf"),

    ("Mathematics", 2026, None, "https://www.uiltexas.org/files/academics/Math_SM_A_26.pdf"),
    ("Mathematics", 2026, None, "https://www.uiltexas.org/files/academics/Math_SM_B_26.pdf"),
    ("Mathematics", 2026, None, "https://www.uiltexas.org/files/academics/Math_SM_D_26.pdf"),

    ("News Writing", 2026, None, "https://www.uiltexas.org/files/academics/News_Contest_InvA_2026_SM.pdf"),
    ("News Writing", 2026, None, "https://www.uiltexas.org/files/academics/News_Contest_InvB_2026_SM.pdf"),
    ("News Writing", 2026, None, "https://www.uiltexas.org/files/academics/News_SM_District_2026.pdf"),

    ("Number Sense", 2026, None, "https://www.uiltexas.org/files/academics/NumberSense_SM_A_26.pdf"),
    ("Number Sense", 2026, None, "https://www.uiltexas.org/files/academics/NumberSense_SM_B_26.pdf"),
    ("Number Sense", 2026, None, "https://www.uiltexas.org/files/academics/NumberSense_SM_D_26.pdf"),

    ("Ready Writing", 2026, None, "https://www.uiltexas.org/files/academics/ReadyWriting_A_26.pdf"),
    ("Ready Writing", 2026, None, "https://www.uiltexas.org/files/academics/ReadyWriting_B_26.pdf"),
    ("Ready Writing", 2026, None, "https://www.uiltexas.org/files/academics/ReadyWriting_SM_Prompts_D_26-Rev2-12.pdf"),

    ("Science", 2026, None, "https://www.uiltexas.org/files/academics/Science_SM_A_26.pdf"),
    ("Science", 2026, None, "https://www.uiltexas.org/files/academics/Science_SM_B_26.pdf"),
    ("Science", 2026, None, "https://www.uiltexas.org/files/academics/Science_SM_D_26.pdf"),

    ("Social Studies", 2026, None, "https://www.uiltexas.org/files/academics/Social_Studies_STUDY_GUIDE_2025-26_updated.pdf"),
    ("Social Studies", 2026, None, "https://www.uiltexas.org/files/academics/Social_Studies_SM_A_26.pdf"),
    ("Social Studies", 2026, None, "https://www.uiltexas.org/files/academics/SocialStudies_SM_B_26.pdf"),
    ("Social Studies", 2026, None, "https://www.uiltexas.org/files/academics/SocialStudies_SM_D_26.pdf"),

    ("Spelling & Vocabulary", 2026, None, "https://www.uiltexas.org/files/academics/Spelling_SM_D_26.pdf"),
]


def dest_path(event: str, year: int, set_code, url: str) -> Path:
    filename = url.split("/")[-1]
    if event == "Computer Science":
        # Match existing structure: Computer Science/2023A/filename.pdf
        folder = BASE / "Computer Science" / f"{year}{set_code}"
    else:
        folder = BASE / event / str(year)
    return folder / filename


def download(url: str, path: Path, dry_run: bool) -> str:
    if path.exists():
        return "skip"
    if dry_run:
        return "dry"
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        path.write_bytes(data)
        return "ok"
    except HTTPError as e:
        return f"HTTP {e.code}"
    except URLError as e:
        return f"ERR {e.reason}"
    except Exception as e:
        return f"ERR {e}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print paths only, no downloads")
    args = parser.parse_args()

    total = len(DOWNLOADS)
    ok = skip = fail = 0

    for i, (event, year, set_code, url) in enumerate(DOWNLOADS, 1):
        path = dest_path(event, year, set_code, url)
        result = download(url, path, args.dry_run)
        label = str(path.relative_to(BASE))
        status = {"ok": "OK", "skip": "--", "dry": "??"}.get(result, "!!")
        print(f"[{i:3}/{total}] {status} {label}" + (f"  ({result})" if result not in ("ok", "skip", "dry") else ""))
        if result == "ok":
            ok += 1
            time.sleep(0.3)   # be polite to UIL server
        elif result == "skip":
            skip += 1
        else:
            fail += 1

    print(f"\nDone. Downloaded: {ok}  Skipped: {skip}  Failed: {fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
