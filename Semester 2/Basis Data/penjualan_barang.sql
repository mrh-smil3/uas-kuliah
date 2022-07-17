-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jul 17, 2022 at 01:54 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `penjualan_barang`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id_barang` int(11) NOT NULL,
  `nama_barang` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id_barang`, `nama_barang`, `harga`, `stock`) VALUES
(1001, 'Printer', 1000000, 10),
(1002, 'Laptop', 10000000, 15),
(1004, 'Monitor', 1500000, 5),
(1005, 'Mouse', 100000, 20),
(1006, 'Keyboard', 150000, 8),
(1007, 'PC', 12000000, 10),
(1008, 'Flashdisk', 50000, 30),
(1009, 'SSD', 500000, 15);

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id_pelanggan` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`id_pelanggan`, `nama`, `alamat`) VALUES
(11290, 'Muhammad Minanul', 'Jepara'),
(11291, 'Rizki Amar', 'Pati'),
(11292, 'Putri Sulistiani', 'Semarang'),
(11293, 'Shintya Firliani', 'Kudus'),
(11294, 'Fitri Kumala', 'Jepara'),
(11295, 'Audrey Jamaludin', 'Pati'),
(11296, 'Febrian Aji', 'Jepara'),
(11297, 'Khoirul Anam', 'Kudus'),
(11298, 'Indah Permata', 'Semarang'),
(11299, 'Adam', 'Kudus');

-- --------------------------------------------------------

--
-- Table structure for table `penjualan`
--

CREATE TABLE `penjualan` (
  `id_transaksi` int(11) NOT NULL,
  `id_pelanggan` int(11) NOT NULL,
  `tgl_transaksi` date NOT NULL,
  `total_trx` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `penjualan`
--

INSERT INTO `penjualan` (`id_transaksi`, `id_pelanggan`, `tgl_transaksi`, `total_trx`) VALUES
(2022001, 11290, '2022-05-02', 1000000),
(2022002, 11299, '2022-05-10', 100000),
(2022003, 11297, '2022-06-29', 11000000),
(2022004, 11291, '2022-05-13', 15000000),
(2022005, 11298, '2022-04-12', 20000000),
(2022006, 11292, '2022-05-25', 10100000),
(2022007, 11293, '2022-05-19', 300000),
(2022008, 11294, '2022-06-06', 24000000),
(2022009, 11295, '2022-06-14', 250000),
(2022010, 11296, '2022-05-24', 2000000);

-- --------------------------------------------------------

--
-- Table structure for table `penjualan_detail`
--

CREATE TABLE `penjualan_detail` (
  `id_transaksi_detail` int(11) NOT NULL,
  `id_transaksi` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `jml_barang` smallint(6) NOT NULL,
  `harga_satuan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `penjualan_detail`
--

INSERT INTO `penjualan_detail` (`id_transaksi_detail`, `id_transaksi`, `id_barang`, `jml_barang`, `harga_satuan`) VALUES
(2424, 2022001, 1002, 1, 10000000),
(2433, 2022002, 1005, 1, 100000),
(2435, 2022003, 1002, 1, 10000000),
(2436, 2022003, 1001, 1, 1000000),
(2437, 2022004, 1007, 1, 12000000),
(2438, 2022004, 1004, 1, 1500000),
(2439, 2022004, 1005, 1, 100000),
(2440, 2022004, 1006, 1, 150000),
(2441, 2022005, 1002, 2, 10000000),
(2442, 2022006, 1002, 1, 10000000),
(2443, 2022006, 1005, 1, 100000),
(2444, 2022007, 1006, 2, 150000),
(2445, 2022008, 1007, 2, 12000000),
(2446, 2022009, 1008, 5, 50000),
(2447, 2022010, 1009, 4, 500000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `penjualan`
--
ALTER TABLE `penjualan`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_pelanggan` (`id_pelanggan`);

--
-- Indexes for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  ADD PRIMARY KEY (`id_transaksi_detail`),
  ADD KEY `id_transaksi` (`id_transaksi`),
  ADD KEY `id_barang` (`id_barang`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id_barang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1010;

--
-- AUTO_INCREMENT for table `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11300;

--
-- AUTO_INCREMENT for table `penjualan`
--
ALTER TABLE `penjualan`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2022011;

--
-- AUTO_INCREMENT for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  MODIFY `id_transaksi_detail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2448;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `penjualan`
--
ALTER TABLE `penjualan`
  ADD CONSTRAINT `penjualan_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`);

--
-- Constraints for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  ADD CONSTRAINT `penjualan_detail_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `penjualan` (`id_transaksi`),
  ADD CONSTRAINT `penjualan_detail_ibfk_2` FOREIGN KEY (`id_barang`) REFERENCES `barang` (`id_barang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
