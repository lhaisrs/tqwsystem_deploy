<h1>Configurações do projeto: </h1>

<p>Antes de iniciar qualquer desenvolvimento do Backend, <a href="https://github.com/TeamWorkQualityReport/TeamWorkQualityReport/blob/master/README.md">configure</a> o seu sistema</p>
<p>Outra forma de configurar o seu ambiente é executando o seguinte comando: </p>
<p><code>pip install -r requirements.txt</code></p>
<p>Pois o arquivo <b>requirements.txt</b> tem todos os dados e versões do sistema que você precisa instalar e configurar o seu sistema.</p>

<h1>Buildando e Rodando a aplicação</h1>

<p>Para rodar/buildar a aplicação, execute o comando abaixo: </p>
<p><code>python manage.py runserver</code></p>

<p><b>Usando o Docker</b></p>
<p>Execute o comando da seção <b>Configuração do Docker</b> no final deste README onde ele executará a migração e o runserver</p>

<h1>Testando via Shell do Python</h1>

<p>Para testar e implementar dados no banco de dados, usamos o Shell do Python e para rodar ele, executamos o comando abaixo:</p>
<p><code>python manage.py shell</code></p>
<p>Após isso, realizamos os testes com cada model importando cada um deles e fazendo as queries desejadas. Vejam alguns exemplos abaixo:</p>
<p>Primeiro, importamos os modelos que queremos realizar a query.</p>
<p><code>from twqsystem.models import Relatorio</code></p>
<p>Depois podemos realizar as queries</p>
<p><code>Relatorio.objects.all()</p></code>
<p><code>Relatorio.objects.create('parametros')</p></code>

<h1>Fazendo migrações no banco</h1>

<p>Após as mudanças feitas no arquivo <b>twqsystem > models.py</b> realize o seguinte comando abaixo para iniciar a migração dos dados para o banco de dados: </p>
<p><code>python manage.py makemigrations</code></p>
<p>Após isso, execute o comando para subir as migrações para o banco de dados: </p>
<p><code>python manage.py migrate</code></p>
<p>Feito a migração! Você já pode testar usando o Shell as novas mudanças. Para subir para o docker faça o passo abaixo.</p>

<p><b>Usando o Docker</b></p>
<p>Execute o comando da seção <b>Configuração do Docker</b> no final deste README onde ele executará a migração e o runserver</p>

<h1>Arquitetura do Sistema: </h1>

<p>Os models foram definidos no arquivo: <b>twqsystem > models.py</b> e foram baseados nos modelos abaixo.</p>

<img src="./images/arquitetura.png">
<img src="./images/modelagem do formulario.jpg">

<p>As configurações de <b>urls.py</b> do projeto estão em <b>teamworkquality > urls.py</b> e da aplicação dos sistemas estão configurados em <b>twqsystem > urls.py</b></p>
<p>Os métodos criados estão no arquivo: <b>twqsystem > views.py</b> e nele há comentários de como cada método e chamada foi implementado.</p>

<p>Obs.: Alguns métodos foram implementados nos models (<b>twqsystem > models.py</b>) usando o decorator <i><b>@classmethod</i></b> para organizar o fluxo de chamada mas as mesmas podem ser realizadas na view</p>

<p>Todos os métodos retornam JSON via HttpRequest ou HttpResponse via uma chamada GET e via uma chamada POST retornam um status do HttpResponseRedirect</p>

<p>O plugin escolhido para exportação de arquivos em <b>PDF</b> é o <b>reportLab</b> que é baixando automaticamente quando realizamos a instalação do requirements.</p>

<p>Para utilização do serviço de email, usamos o próprio SMTP do Django e implementamos no arquivo: <b>twqsystem > views.py</b> pelo método <b>send_relatorio_email</b></p>

<h1>Configuração do DOCKER</h1>
<p>Para facilitar o processo de desenvolvimento e garantir a consistência entre os ambientes.</p>
<p>Antes de qualquer coisa deve-se realizar o download do Docker Community Edition</p>
<p>https://www.docker.com</p>

<p>Uma vez realizado o download e instalação do docker basta executar o seguinte commando na raiz do projeto:</p>
<p><code>docker-compose -f dev.docker-compose.yml up</code></p>

<p>Para testar via Shell no docker, execute os comandos abaixo:</p>
<p><code>docker exec -it teamworkqualityreport_server_1 bash</code></p>
<p><code>cd backend</code></p>
<p><code>python manage.py shell</code></p>

<p>Obs.: Caso ao executar o comando acima tenha dado erro. Para continuar rodando a aplicação sem erros, vá em <b>teamworkquality > settings.py</b> e nas configurações de DATABASES em HOST coloque <b>localhost</b> e não db e execute o comando abaixo que vai estar tudo certo!</p>
<p><code>python manage.py runserver</code></p>