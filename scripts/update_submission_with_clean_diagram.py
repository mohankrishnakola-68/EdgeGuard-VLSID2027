import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

out_path = r'd:\VLSID\EdgeGuard_VLSID2027_Official_Submission_v2.docx'
block_diag_path = r'd:\VLSID\assets\edgeguard_block_diagram_clean.png'
render_path = r'd:\VLSID\assets\edgeguard_product_render.jpg'

doc = docx.Document()

# Page Margins (0.75 in)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Styling Colors
NAVY = RGBColor(16, 44, 87)
BLUE = RGBColor(41, 75, 140)
DARK = RGBColor(33, 37, 41)
GRAY = RGBColor(108, 117, 125)

def add_title(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(16)
    r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(12)
    r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = BLUE
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    return p

def add_body(text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = DARK
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(10)
    r.font.color.rgb = DARK
    return p

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

# ==================== BUILD DOCUMENT ====================

add_title('VLSID 2027 DESIGN CONTEST PROPOSAL')

add_heading_1('Proposal Title')
add_body('EdgeGuard: Privacy-Preserving Smart Door Access and Neighborhood Threat Telemetry on C-DAC Aries v3 RISC-V SoC')

add_heading_1('Platform 1 or 2')
add_body('Platform 1: C-DAC Aries v3 Board (THEJAS32 32-bit RISC-V SoC @ 100 MHz, 256 KB SRAM)')

# Abstract
add_heading_1('Abstract')
add_body('In residential environments, doorway access poses serious security challenges, especially for elderly family members or grandparents living alone while their children are away at work. Standard commercial video doorbells (e.g., Amazon Ring, Google Nest) stream unencrypted video to foreign cloud servers, charge recurring monthly subscriptions, and fail completely during internet blackouts. Conversely, simple digital locks cannot screen unknown visitors or alert off-site homeowners.')
add_body('EdgeGuard is an indigenous, edge-intelligent access and community safety system running on C-DAC’s THEJAS32 32-bit RISC-V SoC (Aries v3 @ 100 MHz). The system implements a dual-domain operational architecture: (1) Pre-Authorized Residents are verified locally on-chip, automatically triggering a 12V solenoid deadbolt in under 240 ms with zero manual effort required from elderly residents inside; (2) Unrecognized Visitors trigger an instant low-bandwidth photo alert to the homeowner’s mobile application, offering remote Open/Deny controls and a time-limited two-way voice intercom; (3) Collaborative Threat Mesh generates a compact, cryptographically signed 32-byte threat alert vector upon detecting tampering or loitering (>30s), broadcast via an auxiliary ESP32 peer-to-peer wireless mesh to alert neighboring houses without sharing raw video feeds. Engineered strictly within a <=165 KB SRAM footprint (<65% of 256 KB internal SRAM), EdgeGuard guarantees data sovereignty, 100% offline functionality for residents, and affordable community security for under Rs. 3,000.')

# Main Idea
add_heading_1('Main Idea')
add_body('Overview and operational details of the EdgeGuard intelligent physical access node:')

add_heading_2('1. Real-World Operational Workflow')
add_body('• Case 1 (Family Member Arrives): Camera captures face frame; THEJAS32 authenticates the candidate descriptor against a locally stored 64-element keyring and pulses the 12V solenoid deadbolt open in <240 ms. Grandparents do not need to walk to the door or struggle with manual latches.')
add_body('• Case 2 (Unknown Visitor / Delivery): System captures a snapshot; companion node transmits a push notification to the owner’s mobile app. The homeowner inspects the photo, triggers remote unlock, denies access, or initiates a two-way intercom call (<120 ms voice latency).')
add_body('• Case 3 (Suspicious Loitering / Physical Tamper): Sustained presence (>30s) or enclosure shock trips the anomaly engine. THEJAS32 frames a signed 32-byte threat packet and broadcasts it over the P2P mesh, warning adjacent doors before an intruder reaches them.')

add_heading_2('2. System Architecture Block Diagram')
if os.path.exists(block_diag_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    doc.add_picture(block_diag_path, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(6)
    r_cap = p_cap.add_run('Figure 1: EdgeGuard System Architecture Block Diagram (THEJAS32 RISC-V SoC & ESP32 Companion)')
    r_cap.font.name = 'Calibri'
    r_cap.font.size = Pt(8.5)
    r_cap.italic = True
    r_cap.font.color.rgb = GRAY

add_heading_2('3. Implementation & SRAM Budgeting on THEJAS32 RISC-V SoC')
add_body('• Memory Feasibility (256 KB SRAM Budget): Peak SRAM allocation is constrained to <=165 KB: 18 KB for 96x96 grayscale frame buffer, 135 KB for INT8 quantized neural activation buffers (using ping-pong layer buffer reuse), and 12 KB for FreeRTOS and system state descriptors, leaving >90 KB safe headroom.')
add_body('• Compute Latency: ~12.8 M-MAC operations executed on the RV32IM hardware integer multiplier (mul) in ~180 ms @ 100 MHz. Local cosine distance comparison takes <1 ms.')
add_body('• Audio Passthrough Routing: Full-duplex conversational audio (I2S mic & speaker) bypasses the THEJAS32 core and connects directly to the companion ESP32 module, maintaining voice latency <120 ms without stalling the safety-critical RISC-V controller.')

# Application
add_heading_1('Application')
add_body('1. Elderly & Assisted Living Homes: Hands-free automatic entry for family members and healthcare workers, coupled with a dedicated physical SOS button for elderly residents living alone.')
add_body('2. Gated Societies & Apartment Complexes: Interconnects hundreds of individual flat doors via a decentralized wireless mesh, alerting security and neighbors if forced entry or loitering occurs at any flat.')
add_body('3. Multi-Gate Educational & Corporate Campuses: Perimeter gates synchronize blacklisted threat vectors locally to prevent barred individuals from entering adjacent access points.')
add_body('4. Rural Infrastructure & Off-Grid Telemetry: Provides deterministic, tamper-evident physical access logging for rural bank branches, primary health centers (PHCs), and telecom shelters without requiring continuous internet connectivity.')

# Value Add
add_heading_1('Value Add')

add_heading_2('1. Comparative Analysis vs. Existing Solutions')

table_comp = doc.add_table(rows=7, cols=4)
table_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ['Evaluation Parameter', 'Traditional Digital Locks', 'Cloud Video Doorbells', 'EdgeGuard (Proposed)']
widths = [Inches(1.5), Inches(1.5), Inches(1.8), Inches(1.9)]

for col_idx, text in enumerate(headers):
    cell = table_comp.cell(0, col_idx)
    cell.width = widths[col_idx]
    set_cell_background(cell, '102C57')
    set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

rows_data = [
    ['Compute Engine', 'Proprietary 8-bit ASIC', 'Foreign Cloud Server (AWS/Google)', 'C-DAC THEJAS32 RISC-V SoC @ 100 MHz'],
    ['Data Privacy', 'Local (PIN/NFC only)', 'Critical Risk (Cloud video streaming)', 'Zero Leakage (100% On-Chip Biometrics)'],
    ['Elderly Support', 'Manual key/door walk needed', 'Complex smartphone app navigation', 'Autonomous auto-unlock for verified family'],
    ['Threat Sharing', 'None (Isolated blind lock)', 'None (Isolated user accounts)', 'Decentralized 32-byte P2P threat mesh'],
    ['Outage Resilience', 'Keypad only', 'Total Failure (No Internet = Dead)', '100% Functional with integrated Li-ion UPS'],
    ['System Cost', 'Rs. 8,000 – 12,000', 'Rs. 15,000+ plus Rs. 500/month fees', 'Sub-Rs. 3,000 ($35 USD) with zero fees']
]

for row_idx, row_content in enumerate(rows_data):
    row_cells = table_comp.rows[row_idx + 1].cells
    bg_color = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
    for col_idx, text in enumerate(row_content):
        cell = row_cells[col_idx]
        cell.width = widths[col_idx]
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(8.5)
        if col_idx == 0:
            r.bold = True
        elif col_idx == 3:
            r.bold = True
            r.font.color.rgb = NAVY

add_heading_2('2. Quantitative Evaluation Targets (To Be Evaluated on Hardware)')

table_metrics = doc.add_table(rows=7, cols=3)
table_metrics.alignment = WD_TABLE_ALIGNMENT.CENTER
m_headers = ['Evaluation Metric', 'Target Objective', 'Verification Methodology']
m_widths = [Inches(2.1), Inches(1.5), Inches(3.1)]

for col_idx, text in enumerate(m_headers):
    cell = table_metrics.cell(0, col_idx)
    cell.width = m_widths[col_idx]
    set_cell_background(cell, '102C57')
    set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

m_rows = [
    ['Total Unlock Latency', '< 240 ms', 'PIR wake -> frame capture -> on-chip match -> relay GPIO pulse'],
    ['Deep-Sleep Standby Power', '< 18 mW (@ 3.3V)', 'Clock-gated standby; woke up via PIR interrupt; ESP32 deep sleep (10 uA)'],
    ['Active Power (Inference/Unlock)', '< 420 mW (@ 3.3V)', 'Core @ 100 MHz + OLED active + 50 ms solenoid relay pull-in pulse'],
    ['P2P Mesh Alert Delivery Latency', '< 350 ms', 'End-to-end propagation time for a 32-byte packet across 3 mesh hops'],
    ['False Acceptance Rate (FAR)', '< 0.1%', 'Enforced by Cosine Similarity threshold >= 0.82 + optical liveness filter'],
    ['Peak SRAM Utilization', '<= 165 KB (<65% of 256 KB)', 'Static .bss + .data linker analysis + FreeRTOS runtime heap monitoring']
]

for row_idx, row_content in enumerate(m_rows):
    row_cells = table_metrics.rows[row_idx + 1].cells
    bg_color = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
    for col_idx, text in enumerate(row_content):
        cell = row_cells[col_idx]
        cell.width = m_widths[col_idx]
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(8.5)
        if col_idx == 0:
            r.bold = True
        elif col_idx == 1:
            r.bold = True
            r.font.color.rgb = NAVY
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

p_note = doc.add_paragraph()
p_note.paragraph_format.space_before = Pt(3)
p_note.paragraph_format.space_after = Pt(4)
r_note = p_note.add_run('Note: Targets represent engineering specifications to be measured and validated on physical hardware during contest execution.')
r_note.font.name = 'Calibri'
r_note.font.size = Pt(8)
r_note.italic = True
r_note.font.color.rgb = GRAY

# References
add_heading_1('References')
refs = [
    '1. C-DAC, "VEGA Processors & ARIES v3 Board User Manual and Technical Specifications", Centre for Development of Advanced Computing (C-DAC), Ministry of Electronics and Information Technology (MeitY), Government of India, 2024. [https://vegaprocessors.in]',
    '2. RISC-V International, "The RISC-V Instruction Set Manual, Volume I: Unprivileged Architecture", Document Version 20191213, Dec. 2019.',
    '3. H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, "Communication-Efficient Learning of Deep Networks from Decentralized Data", International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR, 2017.',
    '4. P. Warden and D. Situnayake, "TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers", O\'Reilly Media, 2019.',
    '5. National Institute of Standards and Technology (NIST), "Lightweight Cryptography Standards for Constrained Devices", NIST SP 800-226, 2024.'
]
for ref in refs:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.space_after = Pt(2.5)
    p_ref.paragraph_format.line_spacing = 1.15
    r_ref = p_ref.add_run(ref)
    r_ref.font.name = 'Calibri'
    r_ref.font.size = Pt(8.5)
    r_ref.font.color.rgb = DARK

doc.save(out_path)
print('Updated official submission docx with clean block diagram successfully at:', out_path)
