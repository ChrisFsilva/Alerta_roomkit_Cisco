<h1 align="center">Helpme - Room kit</h1>			
<br>
<h4 align="center"> 💻 Em produção 💻 </h4>

<div>
  <h1 align="center">Botão de ajuda dos equipamentos Cisco room kit</h1>
<pre>
  <h2 align="center">Sobre o projeto</h2>
   - Layout
   - Como executar o projeto
     - Pré-requisitos
     - Funcionalidades
   - Tecnologias
   - Autor
   - Licença
</pre>
</div>

## Sobre o projeto 

Descrição:
Helpme é uma API desenvolvida para criar um botão de alerta no sistema de video conferencia Cisco room kit. o sistema criará um botão em seu tablet que, ao ser acionado irá disparar automaticamente um alerta a equipe de suporte técnico, dessa forma você facilitará para que o usuarios de sala de video conferencia tenham uma comunicação rapida e pratica a equipe de suporte.

Tecnologias Utilizadas:
JavaScript: Programado totalmente na linguagem
Xapi: Biblioteca utilizada pelo sistema Room Kit
Webhook: Receptor de API

---

## Layout

- Momentaneamente indisponivel

Componentes Principais:
Room kit (Versões mini, kit, pro e plus): Sistema de video conferencia da Cisco.
Webhook: Irá receber as informações da API e transmitir para o power automate, necessario somente se o ambiente do power plataform for fechado pelo Azure
Power Automate: A versão 1.0 da API foi planejada para ser integrada com o power automate em ambiente fechado, o Power automate será responsavel por receber as informações do webhook e irá transmitir os dados em sua rede.

---

## Como executar o projeto

### Pré-requisitos

- Room kit (Versões mini, kit, pro e plus): Sistema de video conferencia da Cisco que contenha tablet.
- Licenciamento do webhook (para ambientes que o power plataform seja fechado)
- Licenciamento do power plataform: Caso seja ambiente aberto você poderá gerar o link diretamente no power automate, excluindo a necessidade do Webhook
  
<b>Instalação:</b>

- Copie o código disponivel em helpme.json
- acesse seu equipamento room kit via IP
- acesse a pagina macros > nova macro
- Cole o código da API e salve a macro
- Vá em layout > Criar botão > ID = nome da macro > Personalize o botão de acordo com o seu desejo

#### Funcionalidades

```bash

Solicitar ajuda:
  Quando o botão for acionado a API irá coletar as informações da sala salvas previamente e transferir para o power automate via webhook, iniciando o fluxo que irá destinar o contato com a equipe técnica.

```

### Guia do Usuário:

``` bash
- Momentaneamente indisponivel
```

## 🛠 Tecnologias

As seguintes tecnologias foram usadas na construção do projeto:

-   **[JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)**
-   **[XAPI](https://xapi.com/)**
-   **[Cisco Room Kit](https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit/model.html)**
-   **[Webhook](https://webhook.site/)**
-   **[Power Automate](https://www.microsoft.com/pt-br/power-platform/products/power-automate)**
---

## 🦸🏻‍♂️ Autor

 <br>
  <sub><b><p>Christopher Silva</p></b></sub></a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Christopher%20Silva-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chris-f-silva//)](https://www.linkedin.com/in/chris-f-silva/) 
[![Gmail Badge](https://img.shields.io/badge/-chrisspfc.silva@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:daniel.rodrigues.soarees@gmail.com)](mailto:chrisspfc.silva@gmail.com)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. [MIT](./LICENSE)

Feito por: Christopher Silva
</div>
