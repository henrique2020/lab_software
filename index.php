<?php
header('Content-type: application/json; charset=utf-8');

$N = 1;

function exibir ($info){
    echo json_encode(["Exec: ". $GLOBALS['N']++ => $info], JSON_PRETTY_PRINT);
    echo PHP_EOL.PHP_EOL;
}

include_once "E:/xampp/htdocs/lab_software/env.php";
include_once ROOT_MODEL . "EquipamentoModelo.php";
include_once ROOT_DAO . "EquipamentoModeloDAO.php";

include_once ROOT_MODEL . "Laboratorio.php";
include_once ROOT_DAO . "LaboratorioDAO.php";

include_once ROOT_MODEL . "Usuario.php";
include_once ROOT_DAO . "UsuarioDAO.php";


$udao = new UsuarioDAO();
$ldao = new LaboratorioDAO();
$edao = new EquipamentoModeloDAO();

/*
$usuario = new Usuario(null, 'Maria Souza', 'maria@email.com', 'Responsavel', null);
exibir($usuario);

$usuario->id = $udao->inserir($usuario);
exibir($usuario);
*/

$usuario = $udao->buscarPorId(3);
exibir($usuario);



/*
$laboratorio = new Laboratorio(null, 'Ladaia', 'LDA', '58', 407);
exibir($laboratorio);

$laboratorio->id = $ldao->inserir($laboratorio);
exibir($laboratorio);
*/

$laboratorio = $ldao->buscarPorId(1);
exibir($laboratorio);

/*
$equipamentoModelo = new EquipamentoModelo(null, 151320, 'ADE 01', 'Dispositivo de corte em grade – 1 mm entre cortes', 'Medtec', 'distância entre cortes de 1mm', 180, 30, 'Digital');
exibir($laboratorio);

$equipamentoModelo->id = $edao->inserir($equipamentoModelo);
exibir($laboratorio);
*/

$equipamentoModelo = $edao->buscarPorId(2);
exibir($equipamentoModelo);
?>