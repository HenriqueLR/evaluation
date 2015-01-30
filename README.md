# Evaluation

Aplicação muito simples, para avaliar um candidato a vaga de programador, entre 0 a 10, em determinadas habilidades, e ao final do processo, será enviado um email,  para o candidato com as informações.

***

### Rodando o projeto


```
obs: Para funcionar corretamente o envio de email, altere a configuração do 
	 "settings.py" de acordo com seu servidor de email, eg: google, postfix, 
	 sendmail etc...
```
   
    EMAIL_HOST = 'server email' 
	EMAIL_PORT = 25
	EMAIL_USE_TLS = False
	EMAIL_HOST_USER= 'user@example.com'

Outra alteranativa, é testar o envio de emails localmente, para isso basta descomentar essa linha no arquivo de configuração.

	EMAIL_BACKEND = 	'django.core.mail.backends.console.EmailBackend'

***

* #####Instalando as dependencias do projeto.
    

		pip install -r requirements.txt


* #####lembretes:
obs: Banco de dados usado, para teste é o sqlite3, mas você pode facilmente configurar outro, como no arquivo de produção "settings_productions.py"
    
    	python manage.py syncdb
    
###Pronto para testar.
    
            python manage.py runserver
