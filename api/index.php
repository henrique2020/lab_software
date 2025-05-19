<?php

header('Content-type: application/json');

$N = 1;
function exibir_json($info){
    echo json_encode($info, JSON_PRETTY_PRINT);
}

/**
 * Recebe um Array e remove os espaços em branco no inicio e fim dos inputs
 */
function clear(array $array): array {
    foreach ($array as $key => $value) {
        $post[$key] = is_array($value) ? clear($value) : (is_string($value) ? trim($value) : $value);
    }
    return $post;
}

include_once "./../env.php";
include_once ROOT_API . "middleware.php";
include_once ROOT_API . "routes.php";

?>