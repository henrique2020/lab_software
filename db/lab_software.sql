-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18/05/2025 às 21:21
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
(1, 'Saúde');

-- --------------------------------------------------------

--
-- Estrutura para tabela `certificado`
--

CREATE TABLE `certificado` (
  `id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `data` date NOT NULL,
  `orgao_expedidor` text NOT NULL,
  `arquivo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamento`
--

CREATE TABLE `equipamento` (
  `id` int(11) NOT NULL,
  `tag` int(11) NOT NULL,
  `numero_patrimonio` int(11) NOT NULL,
  `id_modelo` int(11) NOT NULL,
  `id_laboratorio` int(11) NOT NULL,
  `numero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `critterio_aceitacao_calibracao` text NOT NULL,
  `periodicidade_calibracao` int(11) NOT NULL,
  `periodicidade_manutencao` int(11) NOT NULL,
  `tipo` enum('Analógico','Digital') NOT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `equipamento_modelo`
--

INSERT INTO `equipamento_modelo` (`id`, `numero_patrimonio`, `identificacao`, `equipamento`, `marca`, `critterio_aceitacao_calibracao`, `periodicidade_calibracao`, `periodicidade_manutencao`, `tipo`, `id_categoria`) VALUES
(1, 203673, 'CDI39X00', 'Computador - i3-9X00', 'Dell', 'Tempertatura X com clock em 3,1GHz', 365, 90, 'Digital', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `evento`
--

CREATE TABLE `evento` (
  `id` int(11) NOT NULL,
  `id_equipamento` int(11) NOT NULL,
  `tipo` enum('Calibracao','Manutencao','Qualificacao','Checagem') NOT NULL,
  `data` date NOT NULL,
  `descricao` text DEFAULT NULL,
  `status` enum('Aprovado','Recusado') NOT NULL,
  `custo` decimal(10,2) DEFAULT NULL,
  `id_certificado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `tipo` enum('Administrador','Responsavel') NOT NULL,
  `id_laboratorio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`id`);

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
  ADD UNIQUE KEY `id_certificado` (`id_certificado`),
  ADD KEY `evento_ibfk_1` (`id_equipamento`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `certificado`
--
ALTER TABLE `certificado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `evento`
--
ALTER TABLE `evento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `equipamento`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `equipamento_ibfk_1` FOREIGN KEY (`id_modelo`) REFERENCES `equipamento_modelo` (`id`),
  ADD CONSTRAINT `equipamento_ibfk_2` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);

--
-- Restrições para tabelas `equipamento_modelo`
--
ALTER TABLE `equipamento_modelo`
  ADD CONSTRAINT `equipamento_modelo_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`);

--
-- Restrições para tabelas `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `evento_ibfk_1` FOREIGN KEY (`id_equipamento`) REFERENCES `equipamento` (`id`),
  ADD CONSTRAINT `evento_ibfk_2` FOREIGN KEY (`id_certificado`) REFERENCES `certificado` (`id`);

--
-- Restrições para tabelas `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_laboratorio`) REFERENCES `laboratorio` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
