-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Tempo de geração: 13-Jun-2025 às 15:19
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `lab_software`
--
CREATE DATABASE IF NOT EXISTS `lab_software` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `lab_software`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `bloco`
--

CREATE TABLE `bloco` (
  `id` int(11) NOT NULL,
  `nome` varchar(10) NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `bloco`
--

INSERT INTO `bloco` (`id`, `nome`, `ativo`) VALUES
(1, 'D', 1),
(2, 'G', 1),
(3, 'K', 1),
(4, 'S', 1),
(5, 'U', 1),
(6, 'V', 1),
(7, '72', 1),
(8, '74', 1),
(9, 'CAMVA', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `categoria`
--

INSERT INTO `categoria` (`id`, `nome`, `ativo`) VALUES
(1, 'Balança', 1),
(2, 'Capela', 1),
(3, 'Estufa', 1),
(4, 'Prensa', 1),
(5, 'Termometro', 1),
(6, 'Vidraria', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `certificado`
--

CREATE TABLE `certificado` (
  `id` int(11) NOT NULL,
  `id_evento` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `data` date NOT NULL,
  `orgao_expedidor` text NOT NULL,
  `arquivo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `certificado`
--

INSERT INTO `certificado` (`id`, `id_evento`, `numero`, `data`, `orgao_expedidor`, `arquivo`) VALUES
(1, 1, 213, '2025-05-30', 'FUVEST', '213-fuvest.pdf'),
(2, 2, 1789, '2023-08-20', 'CREA', '1789-crea.pdf');

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipamento`
--

CREATE TABLE `equipamento` (
  `id` int(11) NOT NULL,
  `tag` int(11) NOT NULL,
  `numero_patrimonio` int(11) NOT NULL,
  `data_implantacao` date NOT NULL DEFAULT current_timestamp(),
  `id_modelo` int(11) NOT NULL,
  `id_laboratorio` int(11) NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `equipamento`
--

INSERT INTO `equipamento` (`id`, `tag`, `numero_patrimonio`, `data_implantacao`, `id_modelo`, `id_laboratorio`, `ativo`) VALUES
(1, 9654, 123, '2025-01-01', 1, 1, 1),
(2, 10000, 157, '2024-02-22', 3, 11, 1),
(3, 54138, 62, '2023-08-17', 2, 3, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipamento_modelo`
--

CREATE TABLE `equipamento_modelo` (
  `id` int(11) NOT NULL,
  `numero_patrimonio` int(11) NOT NULL,
  `identificacao` text NOT NULL,
  `equipamento` text NOT NULL,
  `marca` text NOT NULL,
  `criterio_aceitacao_calibracao` text NOT NULL,
  `periodicidade_calibracao` int(11) NOT NULL COMMENT 'Anos',
  `aviso_renovacao_calibracao` int(11) NOT NULL COMMENT 'Dias',
  `periodicidade_manutencao` int(11) NOT NULL COMMENT 'Anos',
  `tipo` enum('A','D') NOT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `equipamento_modelo`
--

INSERT INTO `equipamento_modelo` (`id`, `numero_patrimonio`, `identificacao`, `equipamento`, `marca`, `criterio_aceitacao_calibracao`, `periodicidade_calibracao`, `aviso_renovacao_calibracao`, `periodicidade_manutencao`, `tipo`, `id_categoria`, `ativo`) VALUES
(1, 123456, 'Multímetro', 'Multímetro Digital', 'Fluke', '±2%', 1, 90, 2, 'D', NULL, 1),
(2, 354214, 'BL118', 'Balão volumétrico de 25 mL', 'Brand', '25mL', 5, 90, 10, 'A', NULL, 1),
(3, 489621, 'FIT 06TC', 'Termohigrômetro', 'Minipa', '2ºC; 6ºC; 10ºC; 20ºC; 25ºC, 30ºC; 40ºC; 55ºC', 1, 45, 1, 'D', 5, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `evento`
--

CREATE TABLE `evento` (
  `id` int(11) NOT NULL,
  `id_equipamento` int(11) NOT NULL,
  `tipo` enum('Calibracao','Manutencao','Qualificacao','Verificacao') NOT NULL,
  `data_criacao` datetime NOT NULL DEFAULT current_timestamp(),
  `data_agendada` date NOT NULL,
  `descricao` text NOT NULL,
  `custo` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `evento`
--

INSERT INTO `evento` (`id`, `id_equipamento`, `tipo`, `data_criacao`, `data_agendada`, `descricao`, `custo`) VALUES
(1, 1, 'Calibracao', '2025-06-04 10:48:36', '2025-05-30', 'Vencimento da última calibração', '1299.00'),
(2, 3, 'Calibracao', '2023-08-17 17:02:43', '2023-08-20', 'Calibração necessária para equipamento novo', '2000.00'),
(3, 3, 'Manutencao', '2024-02-23 09:40:00', '2024-03-14', 'Aparelho não estava exibindo as informções', '300.00'),
(4, 3, 'Qualificacao', '2024-04-14 07:11:09', '2024-04-04', '', '749.99');

-- --------------------------------------------------------

--
-- Estrutura da tabela `laboratorio`
--

CREATE TABLE `laboratorio` (
  `id` int(11) NOT NULL,
  `nome` text NOT NULL,
  `sigla` varchar(10) NOT NULL,
  `id_bloco` int(11) NOT NULL,
  `sala` varchar(4) NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `laboratorio`
--

INSERT INTO `laboratorio` (`id`, `nome`, `sigla`, `id_bloco`, `sala`, `ativo`) VALUES
(1, 'Laboratório de Ensaios Mecânicos', 'LAMEC', 1, '101', 1),
(2, 'Laboratório de Materiais', 'LAMAT', 6, '205', 1),
(3, 'Laboratório de Análises e Pesquisas Ambientais', 'LAPAM', 6, '102', 1),
(4, 'Laboratório de Microbiologia Clínica', 'LMC', 4, '105', 1),
(5, 'Laboratório de Controle de Qualidade de Medicamentos e Cosméticos', 'LCMEC', 4, '312', 1),
(6, 'Instituto de Pesquisas em Saúde', 'IPS', 4, '315', 1),
(7, 'Laboratório de Tecnologia Construtiva', 'LBTEC', 3, '105', 1),
(8, 'Laboratório de Corrosão e Proteção Superficial', 'LCOR', 2, '206', 1),
(9, 'Laboratório de Análise e Pesquisa em Alimentos', 'LAPA', 7, '101', 1),
(10, 'Laboratório de Química e Fertilidade do Solo', 'LQFS', 8, '111', 1),
(11, 'Laboratório de Sementes e Fitopatologia', 'LASFI', 9, '105', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` text NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0,
  `id_laboratorio` int(11) DEFAULT NULL,
  `data_acesso` datetime DEFAULT NULL,
  `token` varchar(256) DEFAULT NULL,
  `data_expiracao` datetime DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `email`, `senha`, `admin`, `id_laboratorio`, `data_acesso`, `token`, `data_expiracao`, `ativo`) VALUES
(1, 'Administrador', 'admin@email.com', '$2b$12$LEoOnb5MZYgSQDDTinLP5u/YONrYyfHmMxpxedQBUdsI6YmDZQQMW', 1, NULL, '2025-06-13 08:06:50', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibm9tZSI6IkhlbnJpcXVlIiwiYWRtaW4iOjEsImxhYm9yYXRvcmlvIjpudWxsLCJleHAiOjE3NDk4MjM2MTB9.MThvvka28Eu4gIaCPASz0DxlteI-Qy2bBOZ1WaahLzE', '2025-06-13 14:06:50', 1),
(2, 'Marial de Tal', 'mdt@email.com', '$2b$12$NcqD9yDsMFd72GF/yyrlgu9pJExXpveYhgpFu/cfciT1Ofrc0P7mu', 0, 1, '2025-06-05 20:36:13', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Miwibm9tZSI6Ik1hcmlhbCBkZSBUYWwiLCJhZG1pbiI6MCwibGFib3JhdG9yaW8iOm51bGwsImV4cCI6MTc0OTE3NzM3M30.xc5Ykyht4yfke_I-6PesR7cPz5IHvyxVtEygxx-NvEU', '2025-06-06 02:36:13', 0),
(3, 'Aline Gehlen', 'agehlen1@ucs.br', '$2b$12$sM28NZ099HS4IBdz2Y2LK.LXVmbC6a8n2HsSOruDqh9ulR7pacnhi', 0, 2, NULL, NULL, NULL, 1),
(4, 'Karen Petyele Loreno', 'kploreno@ucs.br', '$2b$12$.UmF.A1NJ8SMi8YQTb62.OwRNdTygy06hNgH9275dGKvnd8Nma9Lm', 0, 3, NULL, NULL, NULL, 1),
(5, 'Claudia Wollheim', 'cwollhei@ucs.br', '$2b$12$QoEAKrRLVEU3oKsRKRsGKe5hrlCFcxlH4BKgsg9kQcFaeQXRfPek6', 0, 4, NULL, NULL, NULL, 1),
(6, 'Juliane Bonfanti da Motta', 'jbmotta@ucs.br', '$2b$12$iuTEz6dXKsmSnwlPPgZnSuXL/8n5Xesw.yT9.JWbFOOH8FEetoHQi', 0, 5, NULL, NULL, NULL, 1),
(7, 'Leonardo Rapone da Motta', 'lrmotta@ucs.br', '$2b$12$sFMqP7hCIKIMYOtgoLr/.uIspr6udbWg2GCR8umqi4QVFYfD37Qye', 0, 6, NULL, NULL, NULL, 1),
(8, 'Cleicimara Ramos Cozen', 'cccolvara@ucs.br', '$2b$12$C8O99KZ39UPGiQ2JKfV2OuPErlJqeBBJXGbZaEYiIfBd4u5Y8KDie', 0, 7, NULL, NULL, NULL, 1),
(9, 'Taís Sabedot Pertile', 'tspertil@ucs.br', '$2b$12$NIekmNQ7v01Tf5sU4q/yKeoMQ227C63TLE5/sNLI7S1IpS/ySA9gK', 0, 8, NULL, NULL, NULL, 1),
(10, 'Daniel Angelo Zattera Milesi', 'dazmiles@ucs.br', '$2b$12$a3LJYez3xMK1f/ohWD3ph.xnfsW6MPRKqZKUZqEOkrNm7n/O/iAxm', 0, 1, NULL, NULL, NULL, 1),
(11, 'Diorvania Ribeiro Giaretta', 'dcribeir@ucs.br', '$2b$12$LDT8mvjK9hXhSxL6RHhuKevah1BRwdj2xw0ZWtwMRNHNcORpV/nR6', 0, 9, NULL, NULL, NULL, 1),
(12, 'Taciane Fulcher Ribeiro', 'tfribeiro@ucs.br', '$2b$12$/dNDtlVjxwqvO1dzsaAm.O8J5y73YMzMsFGPfHwXXWDrzld.OQQgi', 0, 10, NULL, NULL, NULL, 1),
(13, 'Aline Benedetti Bordin', 'abenedet@ucs.br', '$2b$12$tE0rS5yaq6zDdZjinw4etesjupWTa8qKYfVLShSBQjISuQR2KDmLq', 0, 11, NULL, NULL, NULL, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bloco`
--
ALTER TABLE `bloco`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- Índices para tabela `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `certificado_evento` (`id_evento`);

--
-- Índices para tabela `equipamento`
--
ALTER TABLE `equipamento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tag` (`tag`,`numero_patrimonio`),
  ADD KEY `id_modelo` (`id_modelo`),
  ADD KEY `localizacao` (`id_laboratorio`);

--
-- Índices para tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_patrimonio` (`numero_patrimonio`,`identificacao`) USING HASH,
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Índices para tabela `evento`
--
ALTER TABLE `evento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evento_equipamento` (`id_equipamento`);

--
-- Índices para tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_bloco` (`id_bloco`,`sala`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `id_bloco` (`id_laboratorio`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `bloco`
--
ALTER TABLE `bloco`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `certificado`
--
ALTER TABLE `certificado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `evento`
--
ALTER TABLE `evento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `certificado`
--
ALTER TABLE `certificado`
  ADD CONSTRAINT `certificado_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id`);

--
-- Limitadores para a tabela `equipamento`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `equipamento_equipamentoModelo` FOREIGN KEY (`id_modelo`) REFERENCES `equipamento_modelo` (`id`),
  ADD CONSTRAINT `equipamento_laboratorio` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);

--
-- Limitadores para a tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  ADD CONSTRAINT `equipamentoModelo_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`);

--
-- Limitadores para a tabela `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `evento_equipamento` FOREIGN KEY (`id_equipamento`) REFERENCES `equipamento` (`id`);

--
-- Limitadores para a tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  ADD CONSTRAINT `laboratorio_bloco` FOREIGN KEY (`id_bloco`) REFERENCES `bloco` (`id`);

--
-- Limitadores para a tabela `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_laboratorio` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
