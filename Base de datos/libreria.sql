-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2023 a las 20:08:58
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `libreria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `idAdmin` int(11) NOT NULL,
  `NombreAdmin` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `IdAutor` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `copia`
--

CREATE TABLE `copia` (
  `IdCopia` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `Id_EstadoCopia` int(11) NOT NULL,
  `IdLibro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadocopia`
--

CREATE TABLE `estadocopia` (
  `Id_EstadoCopia` int(11) NOT NULL,
  `Nombre_estado` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadocopia`
--

INSERT INTO `estadocopia` (`Id_EstadoCopia`, `Nombre_estado`) VALUES
(1, 'disponible'),
(2, 'en prestamo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadoprestamo`
--

CREATE TABLE `estadoprestamo` (
  `Id_EstadoPrestamo` int(11) NOT NULL,
  `Nombre_estado` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadoprestamo`
--

INSERT INTO `estadoprestamo` (`Id_EstadoPrestamo`, `Nombre_estado`) VALUES
(1, 'al dia'),
(2, 'atrasada'),
(3, 'cerrada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `IdLibro` int(11) NOT NULL,
  `Titulo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libroautor`
--

CREATE TABLE `libroautor` (
  `IdLibro` int(11) NOT NULL,
  `IdAutor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `multa`
--

CREATE TABLE `multa` (
  `IdMulta` int(11) NOT NULL,
  `Monto` int(11) NOT NULL,
  `FechaInicio` date NOT NULL,
  `IdPrestamo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `IdPrestamo` int(11) NOT NULL,
  `FechaInicio` date NOT NULL,
  `FechaFinalizacion` date NOT NULL,
  `IdUsuario` int(11) NOT NULL,
  `IdCopia` int(11) NOT NULL,
  `Id_EstadoPrestamo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipousuario`
--

CREATE TABLE `tipousuario` (
  `Id_TipoUsuario` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipousuario`
--

INSERT INTO `tipousuario` (`Id_TipoUsuario`, `nombre`) VALUES
(1, 'profesor'),
(2, 'alumno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `IdUsuario` int(11) NOT NULL,
  `Rut` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Id_TipoUsuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`idAdmin`);

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`IdAutor`);

--
-- Indices de la tabla `copia`
--
ALTER TABLE `copia`
  ADD PRIMARY KEY (`IdCopia`),
  ADD KEY `fk_estado` (`Id_EstadoCopia`),
  ADD KEY `fklibro` (`IdLibro`);

--
-- Indices de la tabla `estadocopia`
--
ALTER TABLE `estadocopia`
  ADD PRIMARY KEY (`Id_EstadoCopia`);

--
-- Indices de la tabla `estadoprestamo`
--
ALTER TABLE `estadoprestamo`
  ADD PRIMARY KEY (`Id_EstadoPrestamo`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`IdLibro`);

--
-- Indices de la tabla `libroautor`
--
ALTER TABLE `libroautor`
  ADD KEY `fk1` (`IdLibro`),
  ADD KEY `fk2` (`IdAutor`);

--
-- Indices de la tabla `multa`
--
ALTER TABLE `multa`
  ADD PRIMARY KEY (`IdMulta`),
  ADD KEY `fk_idprestamo` (`IdPrestamo`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`IdPrestamo`),
  ADD KEY `fk_idusuario` (`IdUsuario`),
  ADD KEY `fk_idcopia` (`IdCopia`),
  ADD KEY `fk_id_estadoprestamo` (`Id_EstadoPrestamo`);

--
-- Indices de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`Id_TipoUsuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`IdUsuario`),
  ADD KEY `fk_usuario` (`Id_TipoUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `idAdmin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `IdAutor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `copia`
--
ALTER TABLE `copia`
  MODIFY `IdCopia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estadocopia`
--
ALTER TABLE `estadocopia`
  MODIFY `Id_EstadoCopia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `estadoprestamo`
--
ALTER TABLE `estadoprestamo`
  MODIFY `Id_EstadoPrestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `IdLibro` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `multa`
--
ALTER TABLE `multa`
  MODIFY `IdMulta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  MODIFY `IdPrestamo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `Id_TipoUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `IdUsuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `copia`
--
ALTER TABLE `copia`
  ADD CONSTRAINT `fk_estado` FOREIGN KEY (`Id_EstadoCopia`) REFERENCES `estadocopia` (`Id_EstadoCopia`),
  ADD CONSTRAINT `fklibro` FOREIGN KEY (`IdLibro`) REFERENCES `libro` (`IdLibro`);

--
-- Filtros para la tabla `libroautor`
--
ALTER TABLE `libroautor`
  ADD CONSTRAINT `fk1` FOREIGN KEY (`IdLibro`) REFERENCES `libro` (`IdLibro`),
  ADD CONSTRAINT `fk2` FOREIGN KEY (`IdAutor`) REFERENCES `autor` (`IdAutor`);

--
-- Filtros para la tabla `multa`
--
ALTER TABLE `multa`
  ADD CONSTRAINT `fk_idprestamo` FOREIGN KEY (`IdPrestamo`) REFERENCES `prestamo` (`IdPrestamo`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `fk_id_estadoprestamo` FOREIGN KEY (`Id_EstadoPrestamo`) REFERENCES `estadoprestamo` (`Id_EstadoPrestamo`),
  ADD CONSTRAINT `fk_idcopia` FOREIGN KEY (`IdCopia`) REFERENCES `copia` (`IdCopia`),
  ADD CONSTRAINT `fk_idusuario` FOREIGN KEY (`IdUsuario`) REFERENCES `usuario` (`IdUsuario`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`Id_TipoUsuario`) REFERENCES `tipousuario` (`Id_TipoUsuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
