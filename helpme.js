// Invocar biblioteca

import xapi from 'xapi';

 

// Endereço do webhook

const webhookURL = 'https://caminho_da_URL.com'; // substitua pela sua URL do webhook

 

// Ação de clique no botão

xapi.Event.UserInterface.Extensions.Panel.Clicked.on(event => {

  if (event.PanelId === 'helpme') {

    // Dados da sala solicitante

    const payload = {

      room: 'Nome da Sala',

      address: 'Endereço/Andar/Unidade da sala',

      problem: 'Mensagem de alerta'

    };

 

// Ação de POST no webhook

    xapi.Command.HttpClient.Post({

      // Variavel de atalho do webhook

      Url: webhookURL,

      Header: ['Content-Type: application/json'],

      AllowInsecureHTTPS: true

    }, JSON.stringify(payload));

  }

});

 
