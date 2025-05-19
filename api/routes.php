<?php

include_once "./../env.php";

include_once ROOT_DAO . "EquipamentoModeloDAO.php";
include_once ROOT_DAO . "LaboratorioDAO.php";
include_once ROOT_DAO . "UsuarioDAO.php";

$uri = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];

$uri = str_replace('/lab_software', '', $uri);

$udao = new UsuarioDAO();
$ldao = new LaboratorioDAO();
$emdao = new EquipamentoModeloDAO();

$rotaTratada = false;

// Exemplo de rota: GET /api/usuarios
if($method === 'GET'){
    if ($uri === '/api/equipamentos') {
        $informacoes = $emdao->listarTodos();
        $rotaTratada = true;
    }
    else if ($uri === '/api/laboratorios') {
        $informacoes = $ldao->listarTodos();
        $rotaTratada = true;
    }
    else if ($uri === '/api/usuarios') {
        $informacoes = $udao->listarTodos();
        $rotaTratada = true;
    }

    if($rotaTratada){
        exibir_json(['API' => ['URI' => $uri, 'METHOD' => $method], 'DATA' => $informacoes]);
        exit;
    }
}

if($method === 'POST'){
    $dados = clear(json_decode(file_get_contents('php://input'), true));

    if ($uri === '/api/equipamento') {
        $equipamento = new EquipamentoModelo(null, $dados['numero_patrimonio'], $dados['identificacao'], $dados['equipamento'], $dados['marca'], $dados['critterio_aceitacao_calibracao'], $dados['periodicidade_calibracao'], $dados['periodicidade_manutencao'], $dados['tipo'], $dados['categoria']);
        $id = $emdao->inserir($equipamento);
        $rotaTratada = true;
    }
    else if ($uri === '/api/laboratorio') {
        $laboratorio = new Laboratorio(null, $dados['nome'], $dados['sigla'], $dados['bloco'], $dados['sala']);
        $id = $ldao->inserir($laboratorio);
        $rotaTratada = true;
    }
    else if ($uri === '/api/usuario') {
        $usuario = new Usuario(null, $dados['nome'], $dados['email'], $dados['tipo'], $dados['laboratorio']);
        $id = $udao->inserir($usuario);
        $rotaTratada = true;
    }

    if($rotaTratada){
        exibir_json(['succcess' => $id ? true : false]);
        exit;
    }
}

// Rota não encontrada
if(!$rotaTratada){
    http_response_code(404);
    echo json_encode(['erro' => 'Rota não encontrada']);
}
