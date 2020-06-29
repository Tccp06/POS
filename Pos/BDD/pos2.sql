-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 29-06-2020 a las 23:02:20
-- Versión del servidor: 5.5.24-log
-- Versión de PHP: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `pos2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acceso`
--

CREATE TABLE IF NOT EXISTS `acceso` (
  `EmpleadoId` int(3) NOT NULL,
  `Usuario` varchar(10) NOT NULL,
  `Contrasena` varchar(10) NOT NULL,
  KEY `EmpleadoId` (`EmpleadoId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `acceso`
--

INSERT INTO `acceso` (`EmpleadoId`, `Usuario`, `Contrasena`) VALUES
(1, 'admin', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen`
--

CREATE TABLE IF NOT EXISTS `almacen` (
  `ProductoId` int(5) NOT NULL,
  `CantidadProducto` int(5) NOT NULL,
  KEY `ProductoId` (`ProductoId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
  `CategoriaId` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(40) NOT NULL,
  `Descripcion` varchar(60) NOT NULL,
  PRIMARY KEY (`CategoriaId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`CategoriaId`, `Nombre`, `Descripcion`) VALUES
(1, 'prueba', '0'),
(2, 'prueba', 'prueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE IF NOT EXISTS `compra` (
  `CompraId` int(11) NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`CompraId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecompra`
--

CREATE TABLE IF NOT EXISTS `detallecompra` (
  `CompraId` int(11) NOT NULL,
  `ProductoId` int(11) NOT NULL,
  `CantidadProducto` int(11) NOT NULL,
  `NumeroDeArticulos` int(11) NOT NULL,
  `Total` int(11) NOT NULL,
  KEY `ProductoId` (`ProductoId`),
  KEY `CompraId` (`CompraId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE IF NOT EXISTS `empleado` (
  `EmpleadoId` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(15) NOT NULL,
  `Apellido` varchar(15) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Sexo` varchar(10) NOT NULL,
  PRIMARY KEY (`EmpleadoId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`EmpleadoId`, `Nombre`, `Apellido`, `Telefono`, `Sexo`) VALUES
(1, 'admin', 'admin', 123456, 'Femenino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE IF NOT EXISTS `producto` (
  `ProductoId` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(35) NOT NULL,
  `Descripcion` varchar(40) NOT NULL,
  `CategoriaId` int(11) NOT NULL,
  `ProveedorId` int(11) NOT NULL,
  `PrecioUnitarioVenta` int(11) NOT NULL,
  `PrecioUnitarioCompra` int(11) NOT NULL,
  PRIMARY KEY (`ProductoId`),
  KEY `CategoriaId` (`CategoriaId`),
  KEY `ProveedorId` (`ProveedorId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`ProductoId`, `Nombre`, `Descripcion`, `CategoriaId`, `ProveedorId`, `PrecioUnitarioVenta`, `PrecioUnitarioCompra`) VALUES
(2, 'gansito', 'pstelito', 1, 1, 12, 12),
(3, 'pruebaprueba', 'hola ', 1, 1, 12, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE IF NOT EXISTS `proveedor` (
  `ProveedorId` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(30) NOT NULL,
  `Direccion` varchar(60) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Empresa` varchar(30) NOT NULL,
  PRIMARY KEY (`ProveedorId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`ProveedorId`, `Nombre`, `Direccion`, `Telefono`, `Empresa`) VALUES
(1, 'prueba 22', '123hajshd', 1234, 'no hay'),
(2, 'prueba22', 'prueba22', 123, 'no hay');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `acceso`
--
ALTER TABLE `acceso`
  ADD CONSTRAINT `acceso_ibfk_1` FOREIGN KEY (`EmpleadoId`) REFERENCES `empleado` (`EmpleadoId`);

--
-- Filtros para la tabla `almacen`
--
ALTER TABLE `almacen`
  ADD CONSTRAINT `almacen_ibfk_1` FOREIGN KEY (`ProductoId`) REFERENCES `producto` (`ProductoId`);

--
-- Filtros para la tabla `detallecompra`
--
ALTER TABLE `detallecompra`
  ADD CONSTRAINT `detallecompra_ibfk_2` FOREIGN KEY (`CompraId`) REFERENCES `compra` (`CompraId`),
  ADD CONSTRAINT `detallecompra_ibfk_1` FOREIGN KEY (`ProductoId`) REFERENCES `producto` (`ProductoId`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_2` FOREIGN KEY (`ProveedorId`) REFERENCES `proveedor` (`ProveedorId`),
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`CategoriaId`) REFERENCES `categoria` (`CategoriaId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
