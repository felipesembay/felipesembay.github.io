import re
import os

with open('portfolio-churn.html', 'r', encoding='utf-8') as f:
    template_en = f.read()

with open('portfolio-churn-pt.html', 'r', encoding='utf-8') as f:
    template_pt = f.read()

def generate_page(template, is_pt, project_id, title, category, p_type, tech_badges, github_link, description_html):
    content = template

    # Replacements
    if is_pt:
        content = re.sub(r'<title>.*?\| Felipe Sembay</title>', f'<title>{title} | Felipe Sembay</title>', content)
        content = re.sub(r'<h1 class="mb-2 mb-lg-0">.*?</h1>', f'<h1 class="mb-2 mb-lg-0">{title}</h1>', content)
        content = re.sub(r'<li class="current">.*?</li>', f'<li class="current">{title.split(" (")[0]}</li>', content)
        content = re.sub(r'<h2>.*?</h2>', f'<h2>{title}</h2>', content)
    else:
        content = re.sub(r'<title>.*?\| Felipe Sembay</title>', f'<title>{title} | Felipe Sembay</title>', content)
        content = re.sub(r'<h1 class="mb-2 mb-lg-0">.*?</h1>', f'<h1 class="mb-2 mb-lg-0">{title}</h1>', content)
        content = re.sub(r'<li class="current">.*?</li>', f'<li class="current">{title.split(" (")[0]}</li>', content)
        content = re.sub(r'<h2>.*?</h2>', f'<h2>{title}</h2>', content)

    # Lang switcher
    if is_pt:
        content = re.sub(r'href="portfolio-churn\.html"', f'href="portfolio-{project_id}.html"', content)
        content = re.sub(r'href="portfolio-churn-pt\.html"', f'href="portfolio-{project_id}-pt.html"', content)
    else:
        content = re.sub(r'href="portfolio-churn\.html"', f'href="portfolio-{project_id}.html"', content)
        content = re.sub(r'href="portfolio-churn-pt\.html"', f'href="portfolio-{project_id}-pt.html"', content)

    # Images
    content = re.sub(r'assets/img/projects/churn/churn-\d\.png', f'assets/img/projects/{project_id}/1.png', content) # Just generic fallback for now

    # Category, Type, Status, GitHub
    if is_pt:
        content = re.sub(r'<li><strong>Categoria:</strong>.*?</li>', f'<li><strong>Categoria:</strong> {category}</li>', content)
        content = re.sub(r'<li><strong>Tipo:</strong>.*?</li>', f'<li><strong>Tipo:</strong> {p_type}</li>', content)
        content = re.sub(r'<li><strong>GitHub:</strong> <a\s+href=".*?"', f'<li><strong>GitHub:</strong> <a\n                                        href="{github_link}"', content)
    else:
        content = re.sub(r'<li><strong>Category:</strong>.*?</li>', f'<li><strong>Category:</strong> {category}</li>', content)
        content = re.sub(r'<li><strong>Type:</strong>.*?</li>', f'<li><strong>Type:</strong> {p_type}</li>', content)
        content = re.sub(r'<li><strong>GitHub:</strong> <a\s+href=".*?"', f'<li><strong>GitHub:</strong> <a\n                                        href="{github_link}"', content)

    # Tech badges
    tech_html = '\n'.join([f'                                <span class="tech-badge">{tech}</span>' for tech in tech_badges])
    content = re.sub(r'<strong>Tecnologias:</strong><br>\s*(<span class="tech-badge">.*?</span>\s*)+', f'<strong>Tecnologias:</strong><br>\n{tech_html}\n', content)
    content = re.sub(r'<strong>Technologies:</strong><br>\s*(<span class="tech-badge">.*?</span>\s*)+', f'<strong>Technologies:</strong><br>\n{tech_html}\n', content)

    # Description
    if is_pt:
        content = re.sub(r'<div class="portfolio-description".*?</section>', f'<div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">\n{description_html}\n</div>\n</div>\n</div>\n</div>\n</section>', content, flags=re.DOTALL)
    else:
        content = re.sub(r'<div class="portfolio-description".*?</section>', f'<div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">\n{description_html}\n</div>\n</div>\n</div>\n</div>\n</section>', content, flags=re.DOTALL)

    return content


# MATCHSENSE
ms_tech = ['Python', 'Transformers (BERT)', 'React', 'Streamlit', 'NLP', 'FAISS', 'Tailwind', 'Vector DB']
ms_pt_desc = """<h2>MatchSense AI</h2>
<p>Sistema completo de análise semântica para compatibilidade entre currículos e vagas de trabalho, utilizando inteligência artificial e processamento de linguagem natural.</p>
<p>Neste projeto, desenvolvi tanto o motor NLP em Python quanto o protótipo da interface. O sistema utiliza Transformers (Modelo BERT) para extrair o significado real das experiências e habilidades dos candidatos, comparando de forma semântica (e não apenas por palavras-chave) com os requisitos das vagas.</p>
<h4 class="mt-3">Principais Destaques</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Busca Vetorial (FAISS) para matching rápido e escalável.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Extração inteligente de habilidades técnicas e soft skills de PDFs/DOCX.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Arquitetura dividida: Backend em Python e Frontend moderno em React + Tailwind.</li>
</ul>"""

ms_en_desc = """<h2>MatchSense AI</h2>
<p>A complete semantic analysis system for matching resumes and job descriptions using Artificial Intelligence and Natural Language Processing.</p>
<p>In this project, I developed both the NLP engine in Python and the interface prototype. The system uses Transformers (BERT model) to extract the true semantic meaning behind candidates' experiences and skills, comparing them contextually (rather than just through keyword-matching) against job requirements.</p>
<h4 class="mt-3">Key Highlights</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Vector Search (FAISS) for fast and scalable matching.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Intelligent extraction of technical and soft skills from PDFs/DOCX.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Decoupled architecture: Python backend and modern React + Tailwind frontend.</li>
</ul>"""

open('portfolio-matchsense-pt.html', 'w').write(generate_page(template_pt, True, 'matchsense', 'MatchSense AI', 'Machine Learning / NLP', 'Semantic Matching System', ms_tech, 'https://github.com/felipesembay/MatchSense-AI', ms_pt_desc))
open('portfolio-matchsense.html', 'w').write(generate_page(template_en, False, 'matchsense', 'MatchSense AI', 'Machine Learning / NLP', 'Semantic Matching System', ms_tech, 'https://github.com/felipesembay/MatchSense-AI', ms_en_desc))

# KNIGHTS TOUR
kt_tech = ['Python', 'TensorFlow', 'Deep Q-Learning', 'Flask', 'JavaScript', 'HTML/CSS']
kt_pt_desc = """<h2>Cavalo Solitário (Knight's Tour)</h2>
<p>Um jogo clássico de quebra-cabeça de xadrez onde o cavalo deve visitar todas as casas do tabuleiro exatamente uma vez, integrado com Inteligência Artificial baseada em Aprendizado por Reforço (Reinforcement Learning).</p>
<p>A aplicação foi construída com um Frontend em HTML/JS puro para a interatividade do tabuleiro, conectado a um Backend Python vira Flask. A IA foi treinada do zero utilizando o algoritmo Deep Q-Learning (DQN) usando TensorFlow, que sugere os melhores próximos movimentos para o jogador no tabuleiro.</p>
<h4 class="mt-3">Principais Destaques</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Agente de Deep Q-Learning treinado do zero para encontrar os movimentos ótimos em tabuleiros 5x5.</li>
    <li><i class="bi bi-check-circle text-primary"></i> API Flask para servir dicas preditivas da IA em tempo real para a interface de jogo.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Lógica de treinamento customizada implementando a construção do "ambiente" no formato estilo Gym.</li>
</ul>"""

kt_en_desc = """<h2>Knight's Tour (Reinforcement Learning)</h2>
<p>A classic chess puzzle game where the knight must visit every square on the board exactly once, powered by a Reinforcement Learning Artificial Intelligence.</p>
<p>The application features a vanilla HTML/JS frontend for board interactivity, connected to a Python Flask backend. The AI was trained from scratch using the Deep Q-Learning (DQN) algorithm with TensorFlow, which suggests the best optimal next moves directly to the player in real-time.</p>
<h4 class="mt-3">Key Highlights</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Deep Q-Learning agent trained from scratch to find optimal moves on a 5x5 board.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Flask API to serve predictive AI hints in real-time to the web interface.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Custom training loop and environment implementation modeled after OpenAI Gym standards.</li>
</ul>"""

open('portfolio-knightstour-pt.html', 'w').write(generate_page(template_pt, True, 'knightstour', 'Cavalo Solitário (Knight\'s Tour)', 'Reinforcement Learning', 'AI Web Game', kt_tech, 'https://github.com/felipesembay/Knight-s-Tour', kt_pt_desc))
open('portfolio-knightstour.html', 'w').write(generate_page(template_en, False, 'knightstour', 'Knight\'s Tour (RL)', 'Reinforcement Learning', 'AI Web Game', kt_tech, 'https://github.com/felipesembay/Knight-s-Tour', kt_en_desc))

