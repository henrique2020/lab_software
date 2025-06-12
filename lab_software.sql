-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13/06/2025 às 00:49
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

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
-- Estrutura para tabela `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `categoria`
--

INSERT INTO `categoria` (`id`, `nome`) VALUES
(1, 'Balança'),
(2, 'Capela'),
(3, 'Estufa'),
(4, 'Prensa'),
(5, 'Termometro'),
(6, 'Vidraria');

-- --------------------------------------------------------

--
-- Estrutura para tabela `certificado`
--

CREATE TABLE `certificado` (
  `id` int(11) NOT NULL,
  `id_evento` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `data` date NOT NULL,
  `orgao_expedidor` text NOT NULL,
  `arquivo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `certificado`
--

INSERT INTO `certificado` (`id`, `id_evento`, `numero`, `data`, `orgao_expedidor`, `arquivo`) VALUES
(1, 1, 213, '2025-05-30', 'FUVEST', '213-fuvest.pdf');

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamento`
--

CREATE TABLE `equipamento` (
  `id` int(11) NOT NULL,
  `tag` int(11) NOT NULL,
  `numero_patrimonio` int(11) NOT NULL,
  `data_implantacao` date NOT NULL DEFAULT current_timestamp(),
  `id_modelo` int(11) NOT NULL,
  `id_laboratorio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `equipamento`
--

INSERT INTO `equipamento` (`id`, `tag`, `numero_patrimonio`, `data_implantacao`, `id_modelo`, `id_laboratorio`) VALUES
(1, 895123, 8945214, '2024-07-01', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamento_modelo`
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
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `equipamento_modelo`
--

INSERT INTO `equipamento_modelo` (`id`, `numero_patrimonio`, `identificacao`, `equipamento`, `marca`, `criterio_aceitacao_calibracao`, `periodicidade_calibracao`, `aviso_renovacao_calibracao`, `periodicidade_manutencao`, `tipo`, `id_categoria`) VALUES
(1, 123456, 'Multímetro', 'Multímetro Digital', 'Fluke', '±2%', 1, 90, 2, 'D', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `evento`
--

CREATE TABLE `evento` (
  `id` int(11) NOT NULL,
  `id_equipamento` int(11) NOT NULL,
  `tipo` enum('Calibracao','Manutencao','Qualificacao','Verificacao') NOT NULL,
  `data_criacao` datetime NOT NULL DEFAULT current_timestamp(),
  `data_agendada` date NOT NULL,
  `descricao` text NOT NULL,
  `custo` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `evento`
--

INSERT INTO `evento` (`id`, `id_equipamento`, `tipo`, `data_criacao`, `data_agendada`, `descricao`, `custo`) VALUES
(1, 1, 'Calibracao', '2025-06-04 10:48:36', '2025-05-30', 'Vencimento da última calibração', 1299.00);

-- --------------------------------------------------------

--
-- Estrutura para tabela `laboratorio`
--

CREATE TABLE `laboratorio` (
  `id` int(11) NOT NULL,
  `nome` text NOT NULL,
  `sigla` varchar(10) NOT NULL,
  `bloco` varchar(5) NOT NULL,
  `sala` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `laboratorio`
--

INSERT INTO `laboratorio` (`id`, `nome`, `sigla`, `bloco`, `sala`) VALUES
(1, 'Laboratório de Ensaios Mecânicos', 'LAMEC', 'G', '100');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
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
  `data_expiracao` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `email`, `senha`, `admin`, `id_laboratorio`, `data_acesso`, `token`, `data_expiracao`) VALUES
(1, 'Henrique', 'hbh@email.com', '$2b$12$AVR01rsrH7hPYAZlDAIWLu59SxA0LFm84YWKS15lxtXIHXZ0V7FT2', 1, NULL, '2025-06-10 22:19:38', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibm9tZSI6IkhlbnJpcXVlIiwiYWRtaW4iOjEsImxhYm9yYXRvcmlvIjpudWxsLCJleHAiOjE3NDk2MTU1Nzh9.wFnlKU7Ux2ak_AEbryEmH3hoAHMsIpMhT28uWBtPs98', '2025-06-11 04:19:38'),
(2, 'Marial de Tal', 'mdt@email.com', '$2b$12$NcqD9yDsMFd72GF/yyrlgu9pJExXpveYhgpFu/cfciT1Ofrc0P7mu', 0, 1, '2025-06-05 20:36:13', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Miwibm9tZSI6Ik1hcmlhbCBkZSBUYWwiLCJhZG1pbiI6MCwibGFib3JhdG9yaW8iOm51bGwsImV4cCI6MTc0OTE3NzM3M30.xc5Ykyht4yfke_I-6PesR7cPz5IHvyxVtEygxx-NvEU', '2025-06-06 02:36:13');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- Índices de tabela `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `certificado_evento` (`id_evento`);

--
-- Índices de tabela `equipamento`
--
ALTER TABLE `equipamento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tag` (`tag`,`numero_patrimonio`),
  ADD KEY `id_modelo` (`id_modelo`),
  ADD KEY `localizacao` (`id_laboratorio`);

--
-- Índices de tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_patrimonio` (`numero_patrimonio`,`identificacao`) USING HASH,
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Índices de tabela `evento`
--
ALTER TABLE `evento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evento_equipamento` (`id_equipamento`);

--
-- Índices de tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `localizacao` (`bloco`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `id_bloco` (`id_laboratorio`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `certificado`
--
ALTER TABLE `certificado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `evento`
--
ALTER TABLE `evento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `certificado`
--
ALTER TABLE `certificado`
  ADD CONSTRAINT `certificado_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id`);

--
-- Restrições para tabelas `equipamento`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `equipamento_equipamentoModelo` FOREIGN KEY (`id_modelo`) REFERENCES `equipamento_modelo` (`id`),
  ADD CONSTRAINT `equipamento_laboratorio` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);

--
-- Restrições para tabelas `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  ADD CONSTRAINT `equipamentoModelo_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`);

--
-- Restrições para tabelas `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `evento_equipamento` FOREIGN KEY (`id_equipamento`) REFERENCES `equipamento` (`id`);

--
-- Restrições para tabelas `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_laboratorio` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
