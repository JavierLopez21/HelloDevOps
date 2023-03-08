CREATE SCHEMA hello5;

DROP TABLE IF EXISTS hello5.hechos;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE hello5.hechos (
  `row_id` text,
  `cfips` bigint DEFAULT NULL,
  `county` text,
  `state` text,
  `first_day_of_month` text,
  `microbusiness_density` double DEFAULT NULL,
  `active` bigint DEFAULT NULL,
  `id_state` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS hello5.county;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE hello5.county (
  `cfips` bigint DEFAULT NULL,
  `county` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS hello5.estados;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE hello5.estados (
  `id_state` bigint DEFAULT NULL,
  `state` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

