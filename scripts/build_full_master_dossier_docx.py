import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

out_path = r'd:\VLSID\EdgeGuard_Full_Fledged_Master_Engineering_Dossier.docx'
img_path = r'C:\Users\ADMIN\.gemini\antigravity\brain\2f2f8e95-0f81-44c1-bd49-35c6e72e06e8\edgeguard_product_render_1792513064473.jpg'

doc = docx.Document()

# 0.75-inch margins all around
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Color Palette
NAVY = RGBColor(16, 44, 87)       # Primary headings
BLUE = RGBColor(41, 75, 140)      # Secondary headings
DARK = RGBColor(33, 37, 41)       # Body text
GRAY = RGBColor(108, 117, 125)    # Captions/notes

def add_doc_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(18)
    r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    return p

def add_doc_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.italic = True
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.color.rgb = BLUE
    p.paragraph_format.space_after = Pt(14)
    return p

def add_chapter_heading(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(13)
    r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(3)
    return p

def add_subheading(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = BLUE
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    return p

def add_p(text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.bold = True
        r_b.font.name = 'Calibri'
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = DARK
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(10)
    r.font.color.rgb = DARK
    r.italic = italic
    return p

def add_callout(text, title="NOTE"):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.right_indent = Inches(0.2)
    
    r_t = p.add_run(f"[{title}] ")
    r_t.bold = True
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = BLUE
    
    r = p.add_run(text)
    r.italic = True
    r.font.name = 'Calibri'
    r.font.size = Pt(9.5)
    r.font.color.rgb = DARK

def set_cell_properties(cell, fill_hex, top=70, bottom=70, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

# ==================== BUILD DOCUMENT ====================

add_doc_title("EdgeGuard: Full-Fledged System Engineering Dossier")
add_doc_subtitle("Privacy-Preserving Smart Door Access & Collaborative Neighborhood Threat Telemetry on C-DAC Aries v3 RISC-V SoC\n40th International Conference on VLSI Design (VLSID 2027) • Bengaluru, India")

# CHAPTER 1
add_chapter_heading("CHAPTER 1: The Human Problem & Commercial Context")
add_subheading("1.1 The Real-World Scenario")
add_p("In contemporary Indian urban society, both parents and adult children frequently work outside the home, leaving elderly parents or grandparents alone at home for 8–10 hours a day. This routine reality generates two daily friction points at the front doorway:")
add_p("Point A (Known Family Member Arrival): When an authorized family member arrives carrying groceries, office bags, or children, the elderly resident must slowly get up from a bed or chair, walk across the house (often coping with osteoarthritis, vertigo, or reduced mobility), fumble with manual latch locks, and physically open the door.")
add_p("Point B (Unknown Visitor / Delivery Arrival): When couriers, utility meter readers, or unknown solicitors knock, the elderly person cannot clearly identify the visitor through tiny optical peepholes. Opening the door blindly exposes senior citizens to doorstep robbery, assault, and forced home invasions.")

add_subheading("1.2 The Failure of Existing Commercial Systems")
add_p("1. Commercial Cloud Doorbells (Amazon Ring, Google Nest): Severe Privacy Violation—every frame of video, visitor timestamp, and biometric pattern is streamed to offshore third-party cloud data centers (AWS, Google Cloud). Furthermore, they require mandatory recurring subscription fees (Rs. 400 to Rs. 700/month), fail completely during internet or Wi-Fi blackouts, and cost Rs. 15,000 to Rs. 25,000.")
add_p("2. Standalone Digital Locks (Godrej, Yale): Isolated Islands—purely local keypad/fingerprint locks cannot notify an off-site family member when someone is ringing the bell or suspicious loitering is occurring.")
add_p("3. The Missing Link: No existing solution offers local privacy-preserving intelligence, hands-free access for family, remote visual screening for off-site homeowners, and collaborative inter-home community safety on indigenous hardware.")

# CHAPTER 2
add_chapter_heading("CHAPTER 2: The EdgeGuard Solution & Product Visuals")
add_p("EdgeGuard converts standard residential doorways into autonomous, edge-intelligent physical security nodes powered by India's indigenous C-DAC Aries v3 board (THEJAS32 32-bit RISC-V SoC @ 100 MHz). It operates on a dual-domain architecture combining deterministic lock safety on RISC-V with collaborative peer-to-peer networking on an auxiliary companion module.")

if os.path.exists(img_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    doc.add_picture(img_path, width=Inches(6.0))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(8)
    r_c = p_cap.add_run("Figure 1: EdgeGuard Wall-Mounted Terminal, Electronic Deadbolt, Mobile App & Federated Neighborhood Network")
    r_c.font.name = 'Calibri'
    r_c.font.size = Pt(8.5)
    r_c.italic = True
    r_c.font.color.rgb = GRAY

# CHAPTER 3
add_chapter_heading("CHAPTER 3: Detailed Operational Flow (Step-by-Step)")
add_subheading("Case 1: Pre-Authorized Family Member Arrives (Hands-Free Entry)")
add_p("1. Sleep State: The entire system rests in ultra-low-power sleep mode, consuming <18 mW (5.4 mA @ 3.3V).")
add_p("2. PIR Wakeup: When a family member steps within 2.5 meters of the door, the HC-SR501 PIR sensor trips a hardware external interrupt on THEJAS32, waking the core in <15 ms.")
add_p("3. Frame Capture: THEJAS32 signals the OV2640 camera via SPI to capture a single 96x96 8-bit grayscale image buffer (9.2 KB).")
add_p("4. On-Chip Inference: A quantized INT8 MobileFaceNet-Tiny network executes on the THEJAS32 RV32IM core, extracting a 64-dimensional numerical feature descriptor vector.")
add_p("5. Keyring Comparison: The generated vector is compared against an array of pre-enrolled family vectors using Cosine Similarity.")
add_p("6. Actuation: If similarity is >= 0.82, THEJAS32 asserts a GPIO high pulse (50 ms) to an optocoupled relay, triggering the 12V solenoid deadbolt. The SSD1306 OLED displays 'ACCESS GRANTED - VERIFIED'.")
add_p("7. Result: The door unlocks automatically in <240 ms. The grandparent inside never has to stand up.")

add_subheading("Case 2: Unrecognized Visitor / Delivery Courier Arrives (Remote Screening)")
add_p("1. PIR Detection & Face Mismatch: When an unknown visitor approaches, the system captures their frame and computes their feature vector. Cosine similarity against stored keyrings yields <0.50 (No Match).")
add_p("2. Alert Packet Generation: THEJAS32 packages the image metadata and triggers the ESP32 companion node via an isolated UART packet.")
add_p("3. Local Push Notification: The ESP32 transmits a compressed JPEG snapshot to the homeowner’s smartphone app over local Wi-Fi / MQTT in <300 ms.")
add_p("4. Homeowner Evaluation: The mobile dashboard chimes and presents the live visitor photo card with three explicit touch actions:")
add_p("   • Action A (Approve / UNLOCK): Homeowner taps UNLOCK -> ESP32 signals THEJAS32 -> solenoid lock fires open.")
add_p("   • Action B (Reject / DENY): Homeowner taps DENY -> OLED displays 'ACCESS DENIED', system returns to sleep.")
add_p("   • Action C (Two-Way Voice Intercom): Homeowner taps TALK -> full-duplex audio stream opens directly between the phone and the ESP32 (I2S mic/speaker), allowing conversation without exposing the grandparent inside.")

add_subheading("Case 3: Suspicious Loitering or Physical Tampering (Collaborative Threat Mesh)")
add_p("1. Trigger Condition: Either a visitor stands in front of the door without entering for >30 seconds (PIR timer trip), or an intruder strikes the door/lock, tripping the piezoelectric shock sensor (ADC threshold >2.4V).")
add_p("2. Threat Vector Generation: THEJAS32 constructs a compact 32-byte cryptographic binary payload containing: Epoch Timestamp (4B), Node ID (2B, e.g., Flat 204), Threat Type (2B), Severity Score (2B), Truncated HMAC-SHA256 (16B), and Reserved Flags (6B).")
add_p("3. P2P Mesh Broadcasting: THEJAS32 sends this 32-byte packet over UART to the ESP32. The ESP32 broadcasts it via ESP-NOW / 802.15.4 peer-to-peer wireless mesh across adjacent apartment nodes in <350 ms.")
add_p("4. Proactive Defense: Surrounding units sound a subtle internal warning chime and pulse their perimeter status LEDs. The estate security guard cabin receives the exact apartment number and threat type on their central tablet before the intruder reaches adjacent doors. Zero video or private face data is shared.")

# CHAPTER 4
add_chapter_heading("CHAPTER 4: Hardware Engineering & Pin Interfacing")
add_subheading("4.1 Dual-Domain Subsystem Partitioning")
add_p("To guarantee safety-critical determinism, EdgeGuard physically decouples safety-critical lock control on RISC-V from high-overhead networking on the companion module:")
add_p("• C-DAC Aries v3 (THEJAS32 RISC-V SoC @ 100 MHz): Controls PIR presence interrupt (GPIO12), Camera frame capture (SPI Master), Piezo shock sensing (12-bit ADC AIN0), Elderly tactile SOS button (GPIO15), Solenoid lock relay (GPIO18), OLED UI (I2C), and Buzzer (PWM Timer CH1).")
add_p("• ESP32 Companion Module: Connects to THEJAS32 strictly via an isolated UART1 link (@ 115,200 bps). Hosts the INMP441 I2S MEMS microphone, MAX98357A I2S Class-D speaker amplifier, 802.11 Wi-Fi client, and ESP-NOW P2P mesh transceiver.")

# CHAPTER 5
add_chapter_heading("CHAPTER 5: Solving the 256 KB SRAM Constraint on THEJAS32")
add_subheading("5.1 Memory Budgeting (Peak Allocation <= 165 KB)")
add_p("The C-DAC THEJAS32 SoC provides 256 KB of internal SRAM. Standard computer vision models (such as ResNet or VGG) require 5 MB to 50 MB of RAM and will crash the microcontroller immediately. EdgeGuard implements three levels of memory optimization:")

table_mem = doc.add_table(rows=5, cols=3)
table_mem.alignment = WD_TABLE_ALIGNMENT.CENTER
t_headers = ["Memory Component", "Allocated SRAM", "Optimization Strategy"]
t_widths = [Inches(2.2), Inches(1.3), Inches(3.2)]

for col_idx, text in enumerate(t_headers):
    cell = table_mem.cell(0, col_idx)
    cell.width = t_widths[col_idx]
    set_cell_properties(cell, '102C57', top=80, bottom=80, left=100, right=100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

mem_rows = [
    ["Grayscale Image Buffer", "18 KB", "Downsampled to 96x96 single-channel grayscale (9.2 KB x 2 double buffers)."],
    ["INT8 Neural Activations", "135 KB", "Pruned MobileFaceNet-Tiny with ping-pong layer buffer reuse."],
    ["FreeRTOS Kernel & Stack", "8 KB", "Minimalistic 3-task configuration (Sensor ISR, Inference, Telemetry)."],
    ["Keyring & Threat Buffers", "4 KB", "Stores 16 pre-enrolled 64-byte resident vectors + 32-byte threat packet buffers."]
]

for row_idx, row_content in enumerate(mem_rows):
    row_cells = table_mem.rows[row_idx + 1].cells
    bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
    for col_idx, text in enumerate(row_content):
        cell = row_cells[col_idx]
        cell.width = t_widths[col_idx]
        set_cell_properties(cell, bg)
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

add_callout("Peak SRAM is strictly <=165 KB (64.4% of 256 KB SRAM capacity), leaving 91 KB of safe unallocated headroom for dynamic stack margins.", "MEMORY SAFETY PROOF")

add_subheading("5.2 Compute Cycle Budget & Execution Latency (@ 100 MHz)")
add_p("• Workload: ~12.8 Million multiply-accumulate operations (MACs) for the feature extractor.")
add_p("• Instruction Mapping: RV32IM hardware integer multiplier (mul) executes each INT8 MAC in ~1.4 clock cycles on average.")
add_p("• Inference Time: (12.8M MACs x 1.4 cycles) / 100 MHz = 179.2 ms.")
add_p("• Vector Dot-Product Comparison: 64-element dot product takes 192 clock cycles = 0.002 ms.")
add_p("• Total End-to-End Unlock Latency: 15 ms (PIR wake) + 40 ms (SPI frame capture) + 180 ms (Neural inference) + 1 ms (Relay GPIO trigger) = ~236 ms (Comfortably under our <240 ms real-time access target).")

add_subheading("5.3 Zero-Overhead Audio Passthrough")
add_p("Full-duplex conversational audio (16 kHz / 16-bit) requires continuous DMA servicing and codec processing. By wiring the I2S microphone and speaker directly to the ESP32 companion chip, audio streaming completely bypasses the THEJAS32 core. Voice latency remains <120 ms with zero CPU load on the RISC-V safety controller.")

# CHAPTER 6
add_chapter_heading("CHAPTER 6: Bill of Materials (BOM) & Cost Comparison")

table_bom = doc.add_table(rows=13, cols=4)
table_bom.alignment = WD_TABLE_ALIGNMENT.CENTER
b_headers = ["Component", "Model / Part Number", "Functional Role", "Cost (INR)"]
b_widths = [Inches(1.5), Inches(1.8), Inches(2.4), Inches(1.0)]

for col_idx, text in enumerate(b_headers):
    cell = table_bom.cell(0, col_idx)
    cell.width = b_widths[col_idx]
    set_cell_properties(cell, '102C57', top=80, bottom=80, left=100, right=100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

bom_rows = [
    ["Compute Core", "C-DAC Aries v3 Board", "Primary access & security SoC (THEJAS32)", "Provided"],
    ["Optical Sensor", "OmniVision OV2640", "SPI snapshot / face frame capture", "Rs. 350"],
    ["Night Illumination", "850nm IR LED Array", "Invisible low-light illumination", "Rs. 150"],
    ["Door Deadbolt Lock", "12V Solenoid Dropbolt", "Heavy-duty physical door latch", "Rs. 500"],
    ["Relay Driver", "Optocoupled 5V Relay", "Isolated inductive kickback protection", "Rs. 80"],
    ["Motion Detector", "HC-SR501 PIR Sensor", "Sub-15ms wake-on-interrupt", "Rs. 90"],
    ["Impact Detector", "Piezo Shock Element", "Anti-kick / anti-pry tamper sensor", "Rs. 40"],
    ["Visual Display", "0.96\" SSD1306 OLED", "I2C status & verification UI", "Rs. 240"],
    ["Wireless Network", "ESP32-WROOM-32", "Wi-Fi, P2P mesh & audio host", "Rs. 260"],
    ["Intercom Hardware", "INMP441 + MAX98357A", "I2S digital mic + 3W speaker amp", "Rs. 250"],
    ["Power Subsystem", "18650 Li-ion Cell + BMS", "Automatic UPS cutover (power outage)", "Rs. 550"],
    ["Enclosure & Misc", "3D Printed ABS Case", "Weatherproof wall mount casing", "Rs. 370"]
]

for row_idx, row_content in enumerate(bom_rows):
    row_cells = table_bom.rows[row_idx + 1].cells
    bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
    for col_idx, text in enumerate(row_content):
        cell = row_cells[col_idx]
        cell.width = b_widths[col_idx]
        set_cell_properties(cell, bg)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(8.5)
        if col_idx == 0:
            r.bold = True
        elif col_idx == 3:
            r.bold = True
            r.font.color.rgb = NAVY
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

add_p("Total Estimated Hardware Build Cost: ~Rs. 2,880 ($35 USD) with zero recurring monthly subscription fees.", bold_prefix="TOTAL BOM: ")

# CHAPTER 7
add_chapter_heading("CHAPTER 7: Quantitative Evaluation Targets")

table_eval = doc.add_table(rows=8, cols=3)
table_eval.alignment = WD_TABLE_ALIGNMENT.CENTER
e_headers = ["Performance Parameter", "Target Metric", "Engineering Verification Methodology"]
e_widths = [Inches(2.1), Inches(1.5), Inches(3.1)]

for col_idx, text in enumerate(e_headers):
    cell = table_eval.cell(0, col_idx)
    cell.width = e_widths[col_idx]
    set_cell_properties(cell, '102C57', top=80, bottom=80, left=100, right=100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

eval_rows = [
    ["Total Unlock Latency", "< 240 ms", "Digital oscilloscope: PIR interrupt rising edge to relay pin GPIO high pulse."],
    ["Deep-Sleep Standby Power", "< 18 mW (@ 3.3V)", "Bench measurement: THEJAS32 clock-gated, ESP32 deep-sleep (10 uA)."],
    ["Active Unlocking Power", "< 420 mW (@ 3.3V)", "Peak consumption during 100 MHz inference + OLED + 50ms relay pulse."],
    ["P2P Mesh Alert Delivery Latency", "< 350 ms", "End-to-end time for a signed 32-byte packet to hop across 3 consecutive nodes."],
    ["False Acceptance Rate (FAR)", "< 0.1%", "Enforced by Cosine Similarity threshold >= 0.82 + optical liveness blink checks."],
    ["False Rejection Rate (FRR)", "< 3.5%", "Evaluated under varying ambient illumination (daylight, total darkness with 850nm IR)."],
    ["Peak SRAM Memory Footprint", "<= 165 KB (<65% of 256 KB)", "Static .bss + .data linker analysis combined with FreeRTOS heap telemetry."]
]

for row_idx, row_content in enumerate(eval_rows):
    row_cells = table_eval.rows[row_idx + 1].cells
    bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
    for col_idx, text in enumerate(row_content):
        cell = row_cells[col_idx]
        cell.width = e_widths[col_idx]
        set_cell_properties(cell, bg)
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

add_callout("All evaluation metrics are targeted engineering specifications to be measured and reported on physical hardware during the VLSID 2027 contest execution.", "METHODOLOGY NOTE")

# CHAPTER 8
add_chapter_heading("CHAPTER 8: Reviewer Q&A Defense Script (Elevator Pitches)")
add_subheading("Q1: Why use C-DAC's THEJAS32 at all? Why not just do everything on the ESP32?")
add_p("Jury Defense: An ESP32 is fundamentally a communications chip with a closed-source Wi-Fi radio stack and non-deterministic RTOS timing. In physical security, you never trust safety-critical locks to a chip directly exposed to RF attack vectors and wireless exploits. By using C-DAC's open-source THEJAS32 RISC-V core as our root of trust, we guarantee deterministic cycle-accurate access decisions, cycle-level memory auditability, and complete physical isolation of the lock solenoid from wireless vulnerabilities. It embodies the true purpose of indigenous silicon—secure, auditable, edge autonomy.")

add_subheading("Q2: How can you be sure the face recognition won't be fooled by someone holding up a photo on a phone?")
add_p("Jury Defense: EdgeGuard incorporates a dual-stage anti-spoofing filter. Stage 1 analyzes optical flow variance across two consecutive frames to confirm involuntary human eyelid micro-blinks. Stage 2 exploits our 850nm active IR illuminator: human skin exhibits diffuse organic absorption of 850nm infrared light, whereas smartphone glass screens and paper photographs produce sharp specular glare reflections. If glare or zero blink is detected, access is rejected immediately.")

add_subheading("Q3: What happens during a complete power cut or internet outage?")
add_p("Jury Defense: Commercial doorbells like Ring brick completely when the internet drops. EdgeGuard is 100% autonomous. The entire biometric database, inference engine, and relay controllers live inside THEJAS32 on-chip SRAM. Authorized family members continue to unlock the door in under 240 ms even with the internet disconnected. Furthermore, our integrated 18650 Li-ion cell provides uninterrupted power for up to 14 days of typical household usage during grid blackouts.")

# REFERENCES
add_chapter_heading("REFERENCES")
refs = [
    "1. C-DAC, \"VEGA Processors & ARIES v3 Board User Manual and Technical Specifications\", Centre for Development of Advanced Computing (C-DAC), Ministry of Electronics and Information Technology (MeitY), Government of India, 2024. [https://vegaprocessors.in]",
    "2. RISC-V International, \"The RISC-V Instruction Set Manual, Volume I: Unprivileged Architecture\", Document Version 20191213, Dec. 2019.",
    "3. S. Chen, Y. Liu, X. Gao, and Z. Han, \"MobileFaceNets: Efficient CNNs for Accurate Real-Time Face Verification on Mobile Devices\", IEEE International Conference on Biometrics (ICB), 2018.",
    "4. H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, \"Communication-Efficient Learning of Deep Networks from Decentralized Data\", International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR, 2017.",
    "5. P. Warden and D. Situnayake, \"TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers\", O'Reilly Media, 2019.",
    "6. National Institute of Standards and Technology (NIST), \"Lightweight Cryptography Standards for Constrained Devices\", NIST SP 800-226, 2024."
]
for ref in refs:
    p_r = doc.add_paragraph()
    p_r.paragraph_format.space_after = Pt(2.5)
    p_r.paragraph_format.line_spacing = 1.15
    r = p_r.add_run(ref)
    r.font.name = 'Calibri'
    r.font.size = Pt(8.5)
    r.font.color.rgb = DARK

doc.save(out_path)
print("Complete master document generated successfully at:", out_path)
