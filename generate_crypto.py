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
    content = re.sub(r'assets/img/projects/churn/churn-\d\.png', f'assets/img/projects/{project_id}/1.png', content)

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
    content = re.sub(r'<div class="portfolio-description".*?</section>', f'<div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">\n{description_html}\n</div>\n</div>\n</div>\n</div>\n</section>', content, flags=re.DOTALL)

    return content

c_tech = ['Python', 'yfinance', 'Monte Carlo', 'Markowitz', 'PuLP', 'Plotly']

c_pt_desc = '''<h2>Otimização de Portfólio de Criptoativos</h2>
<p>Neste projeto, desenvolvemos um sistema completo de otimização de carteiras focado em criptomoedas, buscando maximizar o retorno ajustado ao risco.</p>
<h4 class="mt-3">Módulos Cobertos</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Coleta e tratamento de dados via <code>yfinance</code>.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Simulação de Monte Carlo para traçar a fronteira eficiente.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Otimização de Markowitz para encontrar o portfólio de Máximo Sharpe e de Mínima Volatilidade.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Métricas de risco completas: Sharpe, Alpha, Beta, VaR, CVaR e Drawdown máximo.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Rebalanceamento inteligente utilizando Programação Linear (PuLP).</li>
    <li><i class="bi bi-check-circle text-primary"></i> Visualizações interativas de alta qualidade com Plotly.</li>
</ul>
<h4 class="mt-4">Resultados das Estratégias</h4>
<div class="table-responsive mt-3">
    <table class="table table-bordered table-hover text-center align-middle">
        <thead class="table-dark">
            <tr>
                <th>Estratégia</th>
                <th>Retorno a.a.</th>
                <th>Volatilidade</th>
                <th>Sharpe</th>
                <th>Max Drawdown</th>
                <th>Capital Final</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Igualitária</strong></td>
                <td>53.18%</td>
                <td>73.87%</td>
                <td>0.652</td>
                <td>-60.06%</td>
                <td>USD 14,784</td>
            </tr>
            <tr>
                <td><strong>Mín. Volatilidade</strong></td>
                <td>59.11%</td>
                <td>58.19%</td>
                <td>0.930</td>
                <td>-50.38%</td>
                <td>USD 18,912</td>
            </tr>
            <tr>
                <td><strong>Máx. Sharpe</strong></td>
                <td>88.20%</td>
                <td>69.80%</td>
                <td>1.192</td>
                <td>-54.83%</td>
                <td>USD 26,239</td>
            </tr>
            <tr>
                <td><strong>PuLP Rebalanceado</strong></td>
                <td>81.77%</td>
                <td>67.93%</td>
                <td>1.130</td>
                <td>-53.55%</td>
                <td>USD 24,307</td>
            </tr>
        </tbody>
    </table>
</div>'''

c_en_desc = '''<h2>Crypto Portfolio Optimization</h2>
<p>In this project, we built a complete portfolio optimization system focused on cryptocurrencies, aiming to maximize risk-adjusted returns.</p>
<h4 class="mt-3">Modules Covered</h4>
<ul>
    <li><i class="bi bi-check-circle text-primary"></i> Data gathering and preprocessing via <code>yfinance</code>.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Monte Carlo Simulation to plot the Efficient Frontier.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Markowitz Optimization to find the Maximum Sharpe and Minimum Volatility portfolios.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Comprehensive risk metrics: Sharpe, Alpha, Beta, VaR, CVaR, and Maximum Drawdown.</li>
    <li><i class="bi bi-check-circle text-primary"></i> Smart Rebalancing using Linear Programming (PuLP).</li>
    <li><i class="bi bi-check-circle text-primary"></i> High-quality interactive visualizations with Plotly.</li>
</ul>
<h4 class="mt-4">Strategy Results</h4>
<div class="table-responsive mt-3">
    <table class="table table-bordered table-hover text-center align-middle">
        <thead class="table-dark">
            <tr>
                <th>Strategy</th>
                <th>Return YoY</th>
                <th>Volatility</th>
                <th>Sharpe</th>
                <th>Max Drawdown</th>
                <th>Final Capital</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Equal-Weight</strong></td>
                <td>53.18%</td>
                <td>73.87%</td>
                <td>0.652</td>
                <td>-60.06%</td>
                <td>USD 14,784</td>
            </tr>
            <tr>
                <td><strong>Min. Volatility</strong></td>
                <td>59.11%</td>
                <td>58.19%</td>
                <td>0.930</td>
                <td>-50.38%</td>
                <td>USD 18,912</td>
            </tr>
            <tr>
                <td><strong>Max. Sharpe</strong></td>
                <td>88.20%</td>
                <td>69.80%</td>
                <td>1.192</td>
                <td>-54.83%</td>
                <td>USD 26,239</td>
            </tr>
            <tr>
                <td><strong>PuLP Rebalanced</strong></td>
                <td>81.77%</td>
                <td>67.93%</td>
                <td>1.130</td>
                <td>-53.55%</td>
                <td>USD 24,307</td>
            </tr>
        </tbody>
    </table>
</div>'''

open('portfolio-financial-risk-pt.html', 'w').write(generate_page(template_pt, True, 'financial-risk', 'Otimização de Portfólio de Criptoativos', 'Analytics / Finanças', 'Otimização de Portfólio', c_tech, 'https://github.com/felipesembay', c_pt_desc))
open('portfolio-financial-risk.html', 'w').write(generate_page(template_en, False, 'financial-risk', 'Crypto Portfolio Optimization', 'Analytics / Finance', 'Portfolio Optimization', c_tech, 'https://github.com/felipesembay', c_en_desc))
