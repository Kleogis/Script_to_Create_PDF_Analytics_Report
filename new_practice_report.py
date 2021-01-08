# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:07:30 2021

@author: Kleogis
"""

from fpdf import FPDF
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_states, plot_countries
from helper import Mode, get_state_names, get_country_names

WIDTH = 210
HEIGHT = 297

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
states=["New Hampshire", "Massachusetts"]

plot_daily_count_states(states, filename = "test.png")
pdf.image("test.png", 5, 30, WIDTH/2-5)
plot_daily_count_countries(["US", "Ukraine"], filename="test2.png")
pdf.image("test2.png", WIDTH/2+5, 30, WIDTH/2-5)

pdf.add_page()

plot_states(states, days=7, filename="test3.png")
pdf.image("test3.png", 5, 10, WIDTH/2-5)

plot_daily_count_states(states, mode=Mode.DEATHS, filename = "test4.png")
pdf.image("test4.png", WIDTH/2+5, 10, WIDTH/2-5)

pdf.output('tuto1.pdf', 'F')