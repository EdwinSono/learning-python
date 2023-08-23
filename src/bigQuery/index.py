from google.cloud import bigquery

def start(request):
  TEXT_LIMIT = 'LIMIT '
  limit = 8
  client = bigquery.Client()
  job_config = bigquery.QueryJobConfig()
  table = "DROP TABLE IF EXISTS `moonei.moonei_b2b.no_clients`; CREATE TABLE `moonei.moonei_b2b.no_clients` AS "  
  resultQuery = 'select * from volumetria'
  QUERY = """
    {}
    WITH
      primer_filtro AS (
          SELECT * FROM `moonei.moonei_b2b.customer` WHERE company_name = "teste123" {}
      ),
      segundo_filtro AS (
          SELECT * FROM `moonei.moonei_b2b.customer` WHERE company_name = "teste1234566666" {}
      ),
      tercer_filtro AS (
          SELECT * FROM `moonei.moonei_b2b.customer` WHERE company_name = "teste" {}
      ),
      volumetria as (
        select (select count(1) from primer_filtro) as count_primerFiltro,
               (select count(1) from segundo_filtro) as count_segundoFiltro,
               (select count(1) from tercer_filtro) as count_tercerFiltro
      )
    {}
  """

  query_job = client.query(QUERY.format("", TEXT_LIMIT + str(limit), "", "", resultQuery), job_config=job_config)  # API request
  results = query_job.result()  # Waits for query to finish

  data1 = 0
  data2 = 0
  data3 = 0

  for row in results:
    data1 = row.count_primerFiltro
    data2 = row.count_segundoFiltro
    data3 = row.count_tercerFiltro
    print("Total rows available: ", data1, data2, data3)

  total = data1 + data2 + data3
  print(total, limit)
  if total <= limit:
    resultQuery = 'select * from primer_filtro UNION ALL SELECT * FROM segundo_filtro UNION ALL SELECT * FROM tercer_filtro'
    query_job = client.query(QUERY.format(table, "", "", "", resultQuery))  # API request
    results = query_job.result()
    print("ejecutar funcion sin limit")
  elif data1 >= limit:
    resultQuery = 'select * from primer_filtro'
    query_job = client.query(QUERY.format(table, TEXT_LIMIT + str(limit), "", "", resultQuery))  # API request
    results = query_job.result()
    print("ejecutar funcion con filtro UNO con limit")
  elif (data1 + data2) >= limit:
    resultQuery = 'select * from primer_filtro UNION ALL SELECT * FROM segundo_filtro'
    query_job = client.query(QUERY.format(table, "", TEXT_LIMIT + str(limit - data1), "", resultQuery))  # API request
    results = query_job.result()
    print("ejecutar funcion con DOS filtros, filtro UNO sin limit, pero función DOS con limit", limit - data1)
  elif (data1 + data2) <= limit:
    resultQuery = 'select * from primer_filtro UNION ALL SELECT * FROM segundo_filtro UNION ALL SELECT * FROM tercer_filtro'
    query_job = client.query(QUERY.format(table, "", "", TEXT_LIMIT + str(limit - (data1 + data2)), resultQuery))  # API request
    results = query_job.result()
    print("ejecutar funcion con los TRES filtros, sin limit las dos primeras y agregando limit a la TERCERA", limit - (data1 + data2))

  for row in results:
    # print(row.company_name)
    print("id={}, company_name={}".format(row[0], row["company_name"]))

start("request")
