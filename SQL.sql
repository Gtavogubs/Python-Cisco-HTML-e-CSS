show databases;

use cruzeiro;
create table jogador(
id int auto_increment primary key,
nome varchar(100) not null,
idade int,
turma varchar(100),
data_cadastro date

);
insert into jogador (nome, idade, turma, data_cadastro) values ('Kaiki Kenji', 29, 'sub20', '1996-02-10'),
('Kaiki',14,'sub16','2011-04-10'),
('Vitor Roque',19,'sub20','2006-02-10'),
('Lucas Silva',15,'sub15','2005-05-10'),
('Fagner Franga',20,'sub20', '2000-09-24'),
('Márcio Luis',30,'profissional', '1990-12-30'),
('Pedro Lucas',20,'profissional','1995-08-03');
select * from jogador;
alter table jogador add column treinador varchar(100);
create table treinador(
id int auto_increment primary key,
nome varchar(100) not null,
idade int,
turma varchar(100),
data_cadastro date
);
insert into treinador (nome, idade, turma, data_cadastro, expertise) values ('Leonardo', 30, 'profissional', '1996-02-10', 'retranca'),
('Seabra', 30, 'sub20', '2000-09-30','ofensivo');
select * from treinador;
alter table treinador rename column expertise to estilo;
create table galinheiro(
id int auto_increment primary key,
nome varchar(100) not null,
idade int,
turma varchar(100),
data_cadastro date
);
alter table treinador add column teste varchar(100);

show tables;
describe jogador;
select * from jogador order by id; 

-- Procedure para listar os jogadores:
delimiter //
CREATE PROCEDURE listar_jogador()
BEGIN
	select * from jogador;
END //

DELIMITER ;

-- para executar:
CALL  listar_jogador();

-- para inserir alunos:
DELIMITER //

CREATE PROCEDURE inserir_jogador(
	IN nome_jogador VARCHAR(100),
    IN idade_jogador INT,
    IN sala_jogador VARCHAR(100),
    IN data_cad DATE,
    IN treinador VARCHAR(100)
)
BEGIN
	INSERT INTO jogador (nome, idade, turma, data_cadastro, treinador)
    VALUES (nome_jogador, idade_jogador, sala_jogador, data_cad, treinador);
END //

DELIMITER ;
drop PROCEDURE inserir_jogador;
-- PARA USAR --

CALL inserir_jogador('Carlos Lima', 20, 'sub20', '2025-03-04' , 'Seabra');

-- procedura para contar treinadores

DELIMITER //

CREATE PROCEDURE contar_treinador(OUT total INT)
BEGIN
	SELECT COUNT(*) INTO total FROM treinador;
END // 

DELIMITER ;

-- Para usar:
CALL contar_treinador(@quantidade);
SELECT @quantidade AS total_treinador;

DELIMITER //

CREATE PROCEDURE atualizar_idade_jogador(
	IN jogador_id INT,
    IN nova_idade INT
)
BEGIN
	UPDATE jogador SET idade = nova_idade WHERE id = jogador_id;
END//

DELIMITER ;
call atualizar_idade_jogador(3, 19);

create table arquivo(
	id int auto_increment primary key,
	nome varchar(100) not null,
	idade INT NOT NULL,
	turma varchar(100),
	data_cadastro date,
    treinador varchar(100)
);

mover o aluno do aluno para o arquivo
DELIMITER //

CREATE PROCEDURE mover_para_Arquivo(IN jogador_id INT)
BEGIN
	INSERT INTO arquivo(nome, idade, turma, data_cadastro, treinador)
    SELECT nome, idade, sala, turma_cadastro, treinador FROM alunos WHERE id = aluno_id;
    
    DELETE FROM jogador WHERE id = jogador_id;
END //

drop PROCEDURE mover_para_arquivo;
DELIMITER ;

-- Para usar:
CALL mover_para_arquivo(4);

create table posicao(
id int auto_increment primary key,
nome_posicao varchar (100) not null,
carga_horario  int 
);
drop table posicao;
insert into Posicao(nome_posicao, carga_horario) values
('Zagueiro', 100),
('Atacante', 240),
('Meia', 240),
('Goleiro', 240),
('Lateral', 1200)
;
create table horario(
    id int auto_increment primary key,
    nome varchar (50),
    turno varchar(20)   -- manha, tarde, noite
   );
insert into horario(nome, turno) values
('7a', 'manha'),
('8b', 'tarde'),
('9A', 'manha');
-- TABELA: matricula(jogador + turma + posicao
create table matriculas(
id int auto_increment primary key,
jogador_id int,
turma_id int,
disciplina_id int,
ano_letivo year,
foreign key (jogador_id) references jogador(id), 
foreign key (turma_id) references turmas(id), 
foreign key (disciplina_id) references disciplina(id)
);
drop table matriculas;
insert into matriculas (jogador_id, turma_id, disciplina_id, ano_letivo) values
(1, 3, 1, 2024),
(2, 2, 2, 2024),
(3, 1, 3, 2024);
create table notas (
id int auto_increment primary key,
jogador_id int,
disciplina_id int,
UC int,
nota decimal (5,2),
foreign key (jogador_id) references jogador(id), 
foreign key (disciplina_id) references disciplina(id)
);
drop table notas;
insert into notas (jogador_id, disciplina_id, UC, nota) values
(1, 1, 1, 7.5),
(1, 1, 2, 8.0),
(2, 2, 1, 6.0);

create table usuarios (
id int auto_increment primary key,
nome_usuarios varchar(100),
email varchar(100) unique,
senha varchar(100),
tipo varchar (20) -- admin, professor, aluno

);
drop table usuarios;
insert into usuarios (nome_usuarios, email, senha, tipo) values
('Administrador', 'Adimin@escola.com', 'admin123', 'admin'),
('joão Santos', 'joao@escola.com', 'aluno123', 'aluno'),
('sergio silva', 'sergio@escola.com', 'prof123', 'professor');

select * from horario;
select * from jogador;
select * from matriculas;
select * from notas;
select * from posicao;
select * from treinador;
select * from usuarios;

-- vamos fazer uma combinação de listas com join

-- seleciona duas colunas: o nome do aluno e o nome da disciplina

SELECT
	jogador.idade as jogador_idade,
 -- Pega o nome da tablea ' alunos' e dá o apelido 'nome_aluno' na saída
	posicao.nome_posicao as posicao
    -- Pega o nome da tabela 'disciplinas' e dá o apelido
    -- 'nome_disciplina' na saída
    
-- Informa de qual tabela vai começar a busca
FROM jogador -- Tabela principal é 'alunpos'

-- Faz a junção da tabela ' matriculas ' com ' alunos '
-- onde o id do aluno é igual ao aluno_id na matrícula
INNER JOIN  matriculas on jogador.id = matriculas.jogador_id

-- Faz a junção databela 'disciplinas' com 'matriculas'
-- onde o id da disciplina é igual ao disciplina_id da matriculaa
INNER JOIN posicao ON matriculas.posicao = posicao.id;


-- Seleciona o nome do professor e o e-mail correspondente
SELECT
	treinador.nome as nome_treinador,
    -- Pega o nome da tabela ' professores ' e renomeia a coluna como 'nome_professor'
    usuarios.email  -- Pega o e-mail da tabela ' usuários '
    
-- Informa de qual tabela principal os dados vão ser buscados
FROM professores -- A consulta começa pela tabela professores

-- Realiza um INNER JOIN com a tabela usuários usando o nome como chave de ligação

INNER JOIN usuarios ON professores.nome = usuarios.nome

-- Aqui está comparando o nome da tabela 'professores' com o nome da tabela 'usuarios'
-- (OBS: Essa ligação por nome não é ideal -- o certo seria usar um ID para garantir consistencia

-- Filtra os resultados para mostrar apenas os registros onde o tipo de usuário é 'professor'
WHERE usuarios.tipo = 'professor';   -- Mostra apenas os usuários que são do tipo professor

DELIMITER ;
-- Verificar idade do aluno
DELIMITER //
CREATE TRIGGER validar_idade_aluno
before insert on alunos
for each row
begin
	if new.idade < 6 then
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Idade mínima para alunos é 6 anos';
	END IF;
END //

CREATE table log_usuarios (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    tipo VARCHAR(20),
    data_cadastro DATETIME
);

DELIMITER // 

CREATE TRIGGER log_novo_usuario
AFTER INSERT ON usuarios
FOR EACH ROW
BEGIN
	INSERT INTO log_usuarios (nome,tipo,data_cadastro)
	VALUES (NEW.nome, NEW.tipo, NOW());
end // 

DELIMITER ;

-- Trigger para atualizar a nota automaticamente oara zero se for nula

DELIMITER //

CREATE TRIGGER nota_padrao
BEFORE INSERT ON notas
for each row
BEGIN
	IF NEW.nota IS NULL THEN
		SET NEW.nota = 0;
	END IF;
END // 

DELIMTIER ;

-- Trigger para impedir exclusão de professores com idade menor que 18
DELIMITER //

CREATE TRIGGER impedir_delete_professor_jovem
BEFORE DELETE ON professores
for each row
begin
	IF OLD.idade < 18 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Não é permitido deletar professores com menos de 18 anos.';
	END IF;
END //

DELIMITER ;


CREATE TABLE notas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    disciplina_id INT,
    bimestre_id INT;
)
