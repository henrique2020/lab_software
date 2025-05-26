<?php

include_once "./../env.php";

function verificarTokenBearer(): void {
    $headers = getallheaders();
    
    if (!isset($headers['Authorization'])) {
        http_response_code(401);
        echo json_encode(['erro' => 'Token não informado']);
        exit;
    }

    $authHeader = $headers['Authorization'];

    if (!preg_match('/Bearer\s(\S+)/', $authHeader, $matches)) {
        http_response_code(401);
        echo json_encode(['erro' => 'Formato de token inválido']);
        exit;
    }

    $token = $matches[1];

    if ($token !== TOKEN) {
        http_response_code(403);
        echo json_encode(['erro' => 'Token inválido']);
        exit;
    }
}