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

if ($method === 'POST' && $uri === '/api/login'){
    $dados = clear(json_decode(file_get_contents('php://input'), true));
    $usuario = $udao->buscarPorEmail($dados['email']);
    if(!is_null($usuario)){
        if($usuario->validatePass($dados['senha'])){
            $usuario->generateToken();
            exibir_json(['API' => ['URI' => $uri, 'METHOD' => $method], 'success' => true, 'token' => $usuario->token]);
        }
    }

    exibir_json(['API' => ['URI' => $uri, 'METHOD' => $method], 'success' => False, 'message' => 'Usuário e/ou senha incorreto']);
}
else if($method === 'GET'){
    verificarTokenBearer();
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
    }
}

if($method === 'POST'){
    verificarTokenBearer();
    $dados = clear(json_decode(file_get_contents('php://input'), true));

    if ($uri === '/api/equipamento') {
        $equipamento = new EquipamentoModelo(null, $dados['numero_patrimonio'], $dados['identificacao'], $dados['equipamento'], $dados['marca'], $dados['criterio_aceitacao_calibracao'], $dados['periodicidade_calibracao'], $dados['periodicidade_manutencao'], $dados['tipo'], $dados['categoria']);
        $id = $emdao->inserir($equipamento);
        $rotaTratada = true;
    }
    else if ($uri === '/api/laboratorio') {
        $laboratorio = new Laboratorio(null, $dados['nome'], $dados['sigla'], $dados['bloco'], $dados['sala']);
        $id = $ldao->inserir($laboratorio);
        $rotaTratada = true;
    }
    else if ($uri === '/api/usuario') {
        $usuario = new Usuario(null, $dados['nome'], $dados['email'], $dados['senha'], $dados['admin'], $dados['laboratorio']);
        $usuario->criptografa();
        $id = $udao->inserir($usuario);
        $rotaTratada = true;
    }

    if($rotaTratada){
        exibir_json(['succcess' => $id ? true : false]);
    }
}

// Rota não encontrada
if(!$rotaTratada){
    http_response_code(404);
    exibir_json(['erro' => 'Rota não encontrada']);
}
