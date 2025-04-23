<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página com Imagem e Legenda</title>
    <style>
        /* Estilos para centralizar a div */
        .container {
            display: flex;
            justify-content: center; /* Centraliza horizontalmente */
            align-items: center; /* Centraliza verticalmente */
            height: 100vh; /* Ocupa toda a altura da tela */
            text-align: center;
        }
        figure {
            margin: 0; /* Remove as margens padrão do <figure> */
        }
        img {
            max-width: 100%; /* Faz a imagem se ajustar ao tamanho da tela */
            height: auto; /* Mantém a proporção da imagem */
        }
    </style>
</head>
<body>
    <div class="container">
        <figure>
            <img src="https://via.placeholder.com/500" alt="Imagem de exemplo">
            <figcaption>Esta é uma legenda da imagem</figcaption>
        </figure>
    </div>
</body>
</html>
