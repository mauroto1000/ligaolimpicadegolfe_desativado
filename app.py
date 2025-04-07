from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Liga Olímpica de Golfe - Novo Endereço</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --green: #00913f;
      --dark: #1e293b;
      --light: #f8fafc;
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, var(--light), #e0f2fe);
      color: var(--dark);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    
    .container {
      width: 100%;
      max-width: 600px;
      padding: 40px;
      background: white;
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    
    .logo-container {
      margin-bottom: 30px;
    }
    
    .logo img {
      max-width: 200px;
      height: auto;
      margin: 0 auto;
    }
    
    .logo-text {
      font-size: 28px;
      font-weight: bold;
      color: var(--primary);
      margin: 20px auto;
    }
    
    h1 {
      color: var(--primary-dark);
      margin-bottom: 30px;
      font-size: 28px;
    }
    
    .new-address {
      font-size: 20px;
      font-weight: 600;
      color: var(--primary);
      margin: 25px 0;
      padding: 15px;
      background-color: rgba(37, 99, 235, 0.1);
      border-radius: 8px;
      display: inline-block;
    }
    
    .btn {
      display: inline-block;
      background: var(--primary);
      color: white;
      text-decoration: none;
      padding: 12px 28px;
      border-radius: 6px;
      font-weight: 600;
      transition: all 0.3s ease;
      margin-top: 10px;
      box-shadow: 0 4px 6px rgba(37, 99, 235, 0.25);
    }
    
    .btn:hover {
      background: var(--primary-dark);
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
    }
    
    .golf-ball {
      position: absolute;
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: white;
      box-shadow: inset -10px -10px 20px rgba(0,0,0,0.1);
      opacity: 0.1;
    }
    
    .ball-1 {
      top: -60px;
      left: -60px;
    }
    
    .ball-2 {
      bottom: -40px;
      right: -40px;
    }
    
    .divider {
      height: 2px;
      background: linear-gradient(to right, transparent, #e5e7eb, transparent);
      margin: 30px 0;
    }
    
    .footer {
      color: #777;
      font-size: 14px;
    }

    /* Ícone de golfe estilizado */
    .golf-icon {
      font-size: 48px;
      color: var(--primary);
      margin-bottom: 15px;
    }
    
    @media (max-width: 576px) {
      .container {
        padding: 30px 20px;
      }
      
      h1 {
        font-size: 24px;
      }
      
      .logo-text {
        font-size: 24px;
      }
      
      .new-address {
        font-size: 18px;
        padding: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="golf-ball ball-1"></div>
    <div class="golf-ball ball-2"></div>
    
    <div class="logo-container">
      <div class="logo">
        <img src="/static/images/logo.png" alt="Logo Liga Olímpica de Golfe" onerror="this.style.display='none'; document.getElementById('logoText').style.display='block';">
        <div id="logoText" class="logo-text" style="display:none;">LIGA OLÍMPICA DE GOLFE</div>
      </div>
    </div>
    
    <h1>A Liga Olímpica de Golfe tem um novo endereço!</h1>
    
    <div class="new-address">
      www.ligaolimpicadegolfe.com.br
    </div>
    
    <a href="https://www.ligaolimpicadegolfe.com.br" class="btn">
      <i class="fas fa-external-link-alt"></i> Acessar novo site
    </a>
    
    <div class="divider"></div>
    
    <p class="footer">
      &copy; 2025 Liga Olímpica de Golfe. Todos os direitos reservados.
    </p>
  </div>
</body>
</html>"""

@app.route('/static/images/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static/images'), filename)

if __name__ == '__main__':
    app.run(debug=True)