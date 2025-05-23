<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://localhost/lab_software/api/equipamento',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "numero_patrimonio": 12345,
    "identificacao": "Multímetro",
    "equipamento": "Multímetro Digital",
    "marca": "Fluke",
    "criterio_aceitacao_calibracao": "±2%",
    "periodicidade_calibracao": "12",
    "periodicidade_manutencao": "24",
    "tipo": "Analógico",
    "categoria": null
}
',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer chave-super-secreta'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
