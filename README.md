# Master's Thesis: Data Modeling in a Cross-domain Ontology for Cyber Intelligence in Smart-Grids Using Reinforcement Learning

The work presents a methodology for integrating power systems and cybersecurity domains using ontological frameworks, with a focus on the Common Information Model (CIM) and the ThreMA cybersecurity framework.

## Thesis Overview

The research develops a systematic approach to link physical power system components with security concepts, such as vulnerabilities and protective measures. This is achieved by establishing formal mappings between CIM power system classes and ThreMA security concepts. The methodology is validated using an enhanced IEEE 9-Bus test system, incorporating realistic network infrastructure and documented attack scenarios.

## Key Contributions

*   **Cross-domain Ontology Integration:** A systematic methodology for bridging the knowledge gap between power engineering and cybersecurity.
*   **Unified Semantic Representation:** A unified data model that connects physical power components with security concepts.
*   **Reinforcement Learning Framework:** An integrated reinforcement learning framework for ontology security and automated anomaly response.
*   **Experimental Validation:** The methodology is validated on an enhanced IEEE 9-Bus test system with realistic attack scenarios.

## Repository Structure

*   `master_thesis_vincenzo_grimaldi.pdf`: The full Master's thesis document.
*   `data/key_details.csv`: Key details extracted from the thesis, including title, author, supervisors, and keywords.
*   `notebooks/01_Verify_Thesis.ipynb`: A Jupyter notebook for step-by-step verification of the thesis details.
*   `notebooks/02_Expertise_Analysis.ipynb`: A Jupyter notebook for analyzing the expertise demonstrated in the thesis and its real-world applications.
*   `plots/`: Contains generated plots for thesis timeline, concept map, and cyber threat landscape.
*   `tests/test_thesis_content.py`: A pytest suite to verify the accuracy of the extracted thesis details.
*   `utils/`: Contains utility scripts for plot generation and other tasks.

## Verification

To verify the contents of this repository, run the following command:

```bash
python3 -m pytest
```

This will execute the test suite and confirm that all extracted details match the information in the thesis document.
