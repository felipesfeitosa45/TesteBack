import pyodbc
server = 'DES-1-135-NOTE\SQLEXPRESS'
database = 'master'
username = 'sa'
password = '4400alc@#'
driver = '{ODBC Driver 11 for SQL Server}'
connection = pyodbc.connect(
    'DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = connection.cursor()

N = int(input('Digite o numero de N:'))

for i in range(N):
    cpf = str(input('Digite o CPF/CNPJ: '))
    nome = str(input('Digite o Nome: '))
    active = str(input('Digite 1 se Ativo e 0 se não:'))
    valor = str(input('Digite o saldo: '))
    sql_command = "INSERT INTO tb_customer_account ( cpf_cnpj, nm_customer, is_active, vl_total) VALUES ( ?, ?, ?, ?); "
    cursor.execute(sql_command, cpf, nome, active, valor )


Media = ("""SELECT Avg(vl_total) AS AveragePrice FROM tb_customer_account Where (vl_total > 560) and
          id_customer BETWEEN 1500 AND 2700;""")
with cursor.execute(Media):
    row = cursor.fetchone()
    while row:
            print("A a média final é: " + str(row[0]))
            row = cursor.fetchone()

print("Os Clintes para média são:")
Clientes = ("""SELECT nm_customer AS [Nome dos Clientes] FROM tb_customer_account Where (vl_total > 560) and 
             id_customer BETWEEN 1500 AND 2700;""")
with cursor.execute(Clientes):
    row = cursor.fetchone()
    while row:
            print(str(row[0]))
            row = cursor.fetchone()

connection.commit()
connection.close()


