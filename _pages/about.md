---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Postdoctoral Fellow at the Center for Research on Microgrids (CROM), Zhejiang University, with a Ph.D. in Electrical Engineering. My work focuses on **multi-energy systems, physics-based modelling, lifecycle energy-carbon assessment, optimization, and energy digitalisation**, with an emphasis on bridging fundamental modelling with practical energy-system applications.

My research has evolved from **intelligent sensing, non-intrusive identification, and fault diagnosis**, to **circular-economy-oriented virtual power plants (CE-cVPP)**, and currently to **Multi-CE-cVPP**, my postdoctoral research framework for park- and community-level multi-energy systems. I develop Python-based computational models and tools that connect equipment physics, thermodynamics, lifecycle assessment, energy/carbon flows, and decision-making, with ongoing work toward interactive digital twins and intelligent energy management.

I am particularly interested in translating rigorous research into **auditable models, computational tools, and deployable solutions** for low-carbon energy systems and industrial digitalisation.

# 🔥 News

- _2026.05_: &nbsp;Released two Multi-CE-cVPP demonstrators: [<strong>SE-LCA</strong>](https://xie-haonan.github.io/Multi-CE-cVPP/selca/) — dynamic lifecycle carbon and exergy-equivalent mapping; [<strong>MEGM</strong>](https://xie-haonan.github.io/Multi-CE-cVPP/megm/) — multi-energy market and hybrid trading layer.
- _2026.03_: &nbsp;Multi-CE-cVPP showcase in active development; full release pending public disclosure.
- _2025.07_: &nbsp;Joined ZJU-Huanjiang Lab as a Postdoctoral Fellow, co-supervised by Prof. Josep M. Guerrero (IEEE Fellow).
- _2025.06_: &nbsp;Earned Ph.D. in Electrical Engineering from Guangxi University.

# 💼 Employments

- _2025.07 - Now_<br>
  **Postdoctoral Fellow**, Center for Research on Microgrids (CROM), Huanjiang Laboratory, Zhejiang University, China.<br>
  **Research Direction**: Multi-energy systems, physics-based modelling, lifecycle energy-carbon assessment, and energy digitalisation.<br>
  **Co-supervisor**: [Prof. Josep M. Guerrero](https://scholar.google.com/citations?user=cj43vw4AAAAJ&hl=en), [Assoc. Prof. Tai Jin](https://scholar.google.com/citations?user=z0ajECcAAAAJ&hl=en)

# 📖 Educations

- _2019.09 - 2025.06_<br>
  **Direct Ph.D.**, School of Electrical Engineering, Guangxi University, China.<br>
  **Research Direction**: Virtual power plant, Energy systems engineering modelling.<br>
  **Supervisor**: [Prof. Hui Hwang Goh](https://scholar.google.com.my/citations?user=bk7OXTsAAAAJ&hl=en) (PhD GPA Ranking **1st/19**).<br>
  **Co-supervisor**: [Prof. Dongdong Zhang](https://ieeexplore.ieee.org/author/37086023621) (Master GPA Ranking **1st/13**)

- _2014.09 - 2018.06_<br>
  **Bachelor**, School of Electrical Engineering, Guangxi University, China.<br>
  **Research Direction**: Power electronics, Control science and engineering (Bachelor GPA Ranking 22nd/160)

# 🌐 Projects

- **Energy–Quality–Carbon Dynamics & Cross-Scale Coordination in Micro-Energy Systems**<br>
  Principal Investigator | China Postdoctoral Science Foundation, General Program | 2026.09–2028.08<br>
  Investigating non-steady-state energy–quality–carbon (EQC) coupling in micro-energy systems under generalized uncertainties, with a focus on generalized thermal inertia, dynamic carbon mapping, and cross-scale coordinated control.<br>
  **Research Focus**: Non-steady-state thermodynamic modelling · Generalized thermal inertia · Energy–quality–carbon mapping · Physics-informed machine learning · Distributionally robust optimization · Model predictive control · RCP-HIL

- **Multi-CE-cVPP — Physics-Informed Multi-Energy Digital Twin Platform**<br>
  Project Lead | Zhejiang University | 2025.07–Present<br>
  Developing a physics-informed digital-twin platform for park- and community-level multi-energy systems, connecting equipment-level physical models, electric/heat/cold carrier flows, stateful storage, simulation services, and interactive visualization.<br>
  **Technical Stack**: Python · FastAPI · React · Three.js · TwinState · REST APIs · Automated Testing · GitHub Actions<br>
  **Public links**: <a href="https://xie-haonan.github.io/Multi-CE-cVPP/" target="_blank" rel="noopener noreferrer">Multi-CE-cVPP Project Portal</a> · <a href="https://github.com/xie-haonan/Multi-CE-cVPP" target="_blank" rel="noopener noreferrer">GitHub/showcase repository</a> · <a href="https://xie-haonan.github.io/Multi-CE-cVPP/selca/" target="_blank" rel="noopener noreferrer">SE-LCA Demo</a> · <a href="https://xie-haonan.github.io/Multi-CE-cVPP/megm/" target="_blank" rel="noopener noreferrer">MEGM Demo</a>.

- **CE-cVPP — Multi-Objective Optimization & Lifecycle Decision Modelling**<br>
  Principal Investigator | Guangxi Graduate Education Innovation Project | 2024.04–2026.04<br>
  Developed a circular-economy-oriented community virtual power plant framework integrating multi-energy system modelling, lifecycle energy, environmental, and economic assessment, prosumer operation, multi-objective optimization, and multi-market interaction.<br>
  **Project No.**: YCBZ2024005<br>
  **Research Focus**: Community Virtual Power Plant · Circular Economy · Lifecycle Assessment · NSGA-II · Multi-Objective Optimization · Energy/Carbon Markets<br>
  **Selected Results**: 67.74% primary-energy saving · 58.68% average pollutant reduction · 55.81% annual lifecycle-cost saving in the load-driven optimized case.<br>
  **Representative papers**: [Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261924005749) · [Renewable and Sustainable Energy Reviews](https://www.sciencedirect.com/science/article/pii/S136403212301047X) · [Process Safety and Environmental Protection](https://www.sciencedirect.com/science/article/pii/S0957582025009954).

- **Intelligent Foreign-Object Detection & Robust Wireless Power Transfer**<br>
  Co-PI | China Southern Power Grid Joint R&D | 2021.12–2023.05<br>
  Built and validated multi-physics and circuit models using ANSYS Maxwell and MATLAB/Simulink to analyse metallic foreign-object impacts on electromagnetic behaviour, coupling, impedance, transmission efficiency, and system stability.<br>
  Supervised the development of data-driven foreign-object detection methods using electrical features, preprocessing, clustering, and learning-based approaches.<br>
  **Selected Outcomes**: Patented technologies · RMB 0.70 million technology-transfer project

- **Power-Quality Analytics & Electrical-Fire Risk Diagnosis**<br>
  Work Package Lead | Ministry of Emergency Management Fire & Rescue R&D Project | 2022.10–2024.09<br>
  Led the power-quality analytics work package covering disturbance denoising, time-frequency detection, feature extraction, and automatic classification under noisy and compound operating conditions.<br>
  **Selected Outcome**: 97.57% average classification accuracy for single disturbances at 30 dB SNR and 94.40% for compound disturbances at 40 dB SNR.

- **3D Energy — UK–China–ASEAN Academic Collaboration**<br>
  China Regional Student Lead | British Council UK–China–BRI Programme | 2021.03–2025.03<br>
  Led a five-member team and coordinated faculty, international visitors, and partner institutions for the end-to-end delivery of China-based programme activities involving 30+ participants.<br>
  Organized international academic seminars, technical workshops, and summit activities on decarbonisation, decentralisation, and digitalisation, facilitating multidisciplinary knowledge exchange and cross-cultural collaboration across the UK, China, and ASEAN partner institutions.

## Other Research Projects

- **Green & Intelligent Distribution Grid Digitalization: Key Technologies and Demonstration** · Guangxi Science and Technology Major Project · 2022.05–2027.04 · **Core Research Team Member**
- **Energy-Efficient Operation of Large Public Buildings Considering Fine-Grained Central Air-Conditioning Energy Flows** · National Natural Science Foundation of China, Young Scientists Fund · 2022.01–2024.12 · **Core Research Team Member**
- **Intelligent Response Technologies for EV Battery-Swap Stations in Vehicle–Grid Interaction** · Guangxi Power Grid Electric Power Research Institute · 2023.12–2024.09 · **Core Research Team Member**
- **Digital Technologies and Big-Data Platform for New Energy Internet of Things** · Ministry of Science and Technology, Belt and Road Project · 2024.01–2025.12 · **Core Research Team Member**
- **Key Technologies and Platform Development for Efficient Coordinated Operation of Integrated Energy Systems** · National Key R&D Program of China · 2020.10–2023.09 · **Core Research Team Member**
- **Key Technologies and Demonstration for Efficient Coordination of Integrated Energy Systems** · National Key R&D Program of China · 2020.12–2023.11 · **Core Research Team Member**
- **Integration of Microgrid and Intelligent Energy Management System** · Guangxi Science & Technology Base and Talent Program · 2019.07–2022.07 · **Core Research Team Member**
- **Synergy of the Future: The Integration of Microgrids and Intelligent Energy Management Systems** · Guangxi Science & Technology Base and Talent Program · 2019.07–2020.07 · **Core Research Team Member**

# 📝 Publications

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->

- Goh HH\*, Huang C, Yew WK, **Xie H**, et al. [Sowing watts, reaping sustainability: Multi-dimensional performance of agrivoltaic electric vehicle charging systems](https://www.sciencedirect.com/science/article/pii/S0957582025013205). **Process Safety and Environmental Protection 2025**. (SCI Q1 Top, IF 6.9)
- **Xie H**, Sun H, Liu H, He T, Goh HH\*, et al. [Prosumer Full Lifecycle Footprint Painting for Circular Economy and Community-Based Virtual Power Plant: A Multi-Objective Optimization Research](https://www.sciencedirect.com/science/article/pii/S0957582025009954). **Process Safety and Environmental Protection 2025**. (SCI Q1 Top, IF 6.9)
- He T, **Xie H**, Goh HH\*, et al. [Advanced sensing and holistic perception technologies for new-type power systems: A comprehensive review](https://www.sciencedirect.com/science/article/pii/S1364032125006963). **Renewable and Sustainable Energy Reviews 2025**. (SCI Q1 Top, IF 16.3)
- Goh HH\*, Liang Q, **Xie H\***, et al. [Maximizing Eco-Energetic and Economic Synergies: Floating Photovoltaic Engaged Pumped-Hydro Energy Storage for Water Scarcity Alleviation, Carbon Emission Reduction, and Cost Efficiency](https://www.sciencedirect.com/science/article/pii/S0957582025003490). **Process Safety and Environmental Protection 2025**. (SCI Q1 Top, IF 6.9)
- Goh HH, Huang C, Liang X, **Xie H\***, et al., [Sustainable Development through the Balancing of Photovoltaic Charging Facilities and Agriculture for Energy Harvesting](https://www.sciencedirect.com/science/article/pii/S0306261924018464). **Applied Energy 2025**. (SCI Q1 Top, IF 10.1)
- **Xie H**, Goh HH\*, Zhang DD\*, et al. [Eco-Energetical Analysis of Circular Economy and Community-Based Virtual Power Plants (CE-cVPP): A Systems Engineering-Engaged Life Cycle Assessment (SE-LCA) Method for Sustainable Renewable Energy Development](https://www.sciencedirect.com/science/article/pii/S0306261924005749). **Applied Energy 2024**. (SCI Q1 Top, IF 11.2)
- **Xie H**, Ahmad T, Zhang DD\*, Goh HH\*, Wu T\*. [Community-based Virtual Power Plants’ Technology and Circular Economy Models in the Energy Sector: A Techno-Economy Study](https://www.sciencedirect.com/science/article/pii/S136403212301047X). **Renewable and Sustainable Energy Reviews 2024**. (SCI Q1 Top, IF 16.79)
- **Xie H**, Sun H, Zhang D, Wong SY, Goh HH\*. [The Integration of Supercritical and Reheating Rankine Cycles in Advanced Thermal Energy Systems for Extreme Weather Adaptation](https://www.energy-proceedings.org/the-integration-of-supercritical-and-reheating-rankine-cycles-in-advanced-thermal-energy-systems-for-extreme-weather-adaptation/). **16th International Conference on Applied Energy 2024**.
- Yin J\*, **Xie H**, Goh HH, Dai W. [Unveiling the Hidden Dangers by Investigating the Relationship Between Low-Voltage Power Quality and Electrical Fire](https://ieeexplore.ieee.org/document/10693221). **3rd International Conference on Energy and Electrical Power Systems 2024**. (EI)
- **Xie H**, Jiang M, Zhang D\*, Goh HH\*, Ahmad T, Liu H, et al. [IntelliSense Technology in the New Power Systems](https://www.sciencedirect.com/science/article/pii/S1364032123000850). **Renewable and Sustainable Energy Reviews 2023**. (SCI Q1 Top, IF 16.79, 🔔ESI Highly Cited)
- **Xie H**, Huang R, Sun H, Han Z, Jiang M, Zhang D\*, Goh HH\*, et al. [Wireless Energy: Paving the Way for Smart Cities and a Greener Future](https://www.sciencedirect.com/science/article/pii/S0378778823006990). **Energy and Buildings 2023**. (SCI Q1 Top, IF 6.7)
- Xiao J, Yin L, **Xie H\***, Huang R, Zhang D, Wu T. [A parametric Modeling Method for Planar Coil Design in Wireless Power Transfer](https://ieeexplore.ieee.org/document/9846257/). **IEEE 5th International Electrical and Energy Conference 2022**.

# 📜 Patents/Software Copyright

- **Xie H**, Huang R, Sun H, Liu H, Jin T, Li BH, Tang DG, Wu HZ, Guerrero JM, A modeling method for circular operation of energy systems based on ecological economic theory. CN Invention Patent Application (Published), 2026, CN202610063913.0.
- **Xie H**, Huang R, Sun H, Liu H, Jin T, Li BH, Tang DG, Wu HZ, Guerrero JM, A method for quantitative assessment of energy system sustainability. CN Invention Patent Application (Published), 2026, CN202610063915.X.
- Zhang D, **Xie H**, Huang R, et al., A High Power Density Electromagnetic Equipment Operation Test Platform. CN Patent, 2022, CN216117849U.
- Zhang D, **Xie H**, Guo P, et al., A near-field wireless charging and maximum power tracking control system and method based on position control. CN Patent, 2021, CN202110970936.7.
- Zhang D, **Xie H**, Sun H, et al., A non-invasive identification method, system, device, and storage medium for electromagnetic equipment with multiple parameters based on integrated algorithms. CN Patent, 2021, CN202110983345.3.
- Sun H, **Xie H**. DNA Sensitive Sequence Filtering Software. CN Computer Software Copyright, 2021, 2021SR0683801.
- **Xie H**, Sun H. CMSEIRD Infectious Disease Prediction System. CN Computer Software Copyright, 2020, 2020R11L2661762.

# 🎖 Honors and Awards

- **Outstanding Doctoral** Graduate Award of Guangxi University, 2025.
- **National Scholarship** for Doctoral Students, 2024.
- **Outstanding Doctoral Award** of China Electrotechnical Society, 2023.
- **Silver Award** of the 9th China International "Internet +" Undergraduate Innovation and Entrepreneurship Competition in Guangxi, 2023. (8th/15)
- **Outstanding Students** of Guangxi University, 2022-2024. (2 times)
- **The First Prize Graduate Academic Scholarship** of Guangxi University, 2019-2024. (4 times)
- **The Second Prize Graduate Academic Scholarship** of Guangxi University, 2019-2024. (2 times)
- **The First Prize Academic Scholarship** of Guangxi University, 2014-2018. (4 times)
- **National Encouragement Scholarship** of China, 2014-2018. (2 times)
