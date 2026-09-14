--
-- PostgreSQL database dump
--

\restrict 66syfwsMRZW7iWOxpJiYp3s7j0o6pHwDWeszVf97TdvveXJnbjxfNNxQaal7Bwf

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-09-14 00:07:42

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16543)
-- Name: classificacao_atual; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classificacao_atual (
    id integer NOT NULL,
    temporada integer NOT NULL,
    posicao integer NOT NULL,
    "time" character varying(100) NOT NULL,
    pontos integer NOT NULL,
    jogos integer NOT NULL,
    vitorias integer NOT NULL,
    empates integer NOT NULL,
    derrotas integer NOT NULL,
    gols_pro integer NOT NULL,
    gols_contra integer NOT NULL,
    atualizado_em timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.classificacao_atual OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16542)
-- Name: classificacao_atual_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classificacao_atual_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classificacao_atual_id_seq OWNER TO postgres;

--
-- TOC entry 5026 (class 0 OID 0)
-- Dependencies: 221
-- Name: classificacao_atual_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classificacao_atual_id_seq OWNED BY public.classificacao_atual.id;


--
-- TOC entry 220 (class 1259 OID 16520)
-- Name: historico_brasileirao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.historico_brasileirao (
    id integer NOT NULL,
    temporada smallint NOT NULL,
    posicao smallint NOT NULL,
    "time" character varying(100) NOT NULL,
    pontos smallint NOT NULL,
    jogos smallint NOT NULL,
    vitorias smallint NOT NULL,
    empates smallint NOT NULL,
    derrotas smallint NOT NULL,
    gols_pro smallint NOT NULL,
    gols_contra smallint NOT NULL,
    saldo_gols smallint NOT NULL,
    CONSTRAINT posicao_valida CHECK (((posicao >= 1) AND (posicao <= 20))),
    CONSTRAINT temporada_valida CHECK (((temporada >= 2021) AND (temporada <= 2025)))
);


ALTER TABLE public.historico_brasileirao OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16519)
-- Name: historico_brasileirao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.historico_brasileirao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.historico_brasileirao_id_seq OWNER TO postgres;

--
-- TOC entry 5027 (class 0 OID 0)
-- Dependencies: 219
-- Name: historico_brasileirao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.historico_brasileirao_id_seq OWNED BY public.historico_brasileirao.id;


--
-- TOC entry 4860 (class 2604 OID 16546)
-- Name: classificacao_atual id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classificacao_atual ALTER COLUMN id SET DEFAULT nextval('public.classificacao_atual_id_seq'::regclass);


--
-- TOC entry 4859 (class 2604 OID 16523)
-- Name: historico_brasileirao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historico_brasileirao ALTER COLUMN id SET DEFAULT nextval('public.historico_brasileirao_id_seq'::regclass);


--
-- TOC entry 5020 (class 0 OID 16543)
-- Dependencies: 222
-- Data for Name: classificacao_atual; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.classificacao_atual (id, temporada, posicao, "time", pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, atualizado_em) FROM stdin;
21	2026	1	Flamengo	54	26	16	6	4	51	21	2026-09-10 00:33:57.295601
22	2026	2	Palmeiras	53	26	15	8	3	45	21	2026-09-10 00:33:57.295601
23	2026	3	Athletico Paranaense	45	26	13	6	7	38	28	2026-09-10 00:33:57.295601
24	2026	4	Fluminense	45	26	12	9	5	40	32	2026-09-10 00:33:57.295601
25	2026	5	Bahia	43	26	11	10	5	40	32	2026-09-10 00:33:57.295601
26	2026	6	Cruzeiro	42	26	12	6	8	38	37	2026-09-10 00:33:57.295601
27	2026	7	Coritiba	37	26	10	7	9	34	35	2026-09-10 00:33:57.295601
28	2026	8	Atletico-MG	36	25	10	6	9	32	30	2026-09-10 00:33:57.295601
29	2026	9	RB Bragantino	35	25	10	5	10	31	28	2026-09-10 00:33:57.295601
30	2026	10	São Paulo FC	33	25	9	6	10	31	28	2026-09-10 00:33:57.295601
31	2026	11	Vitoria	32	26	9	5	12	25	37	2026-09-10 00:33:57.295601
32	2026	12	Corinthians	32	26	8	8	10	27	27	2026-09-10 00:33:57.295601
33	2026	13	Santos	32	25	8	8	9	37	38	2026-09-10 00:33:57.295601
34	2026	14	Botafogo	31	25	8	7	10	37	40	2026-09-10 00:33:57.295601
35	2026	15	Gremio	28	25	7	7	11	27	33	2026-09-10 00:33:57.295601
36	2026	16	Mirassol	28	26	7	7	12	29	40	2026-09-10 00:33:57.295601
37	2026	17	Vasco DA Gama	25	25	6	7	12	27	40	2026-09-10 00:33:57.295601
38	2026	18	Internacional	25	26	5	10	11	28	34	2026-09-10 00:33:57.295601
39	2026	19	Remo	23	26	5	8	13	30	43	2026-09-10 00:33:57.295601
40	2026	20	Chapecoense	17	25	3	8	14	27	50	2026-09-10 00:33:57.295601
\.


--
-- TOC entry 5018 (class 0 OID 16520)
-- Dependencies: 220
-- Data for Name: historico_brasileirao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.historico_brasileirao (id, temporada, posicao, "time", pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols) FROM stdin;
1	2021	1	Atlético-MG	84	38	26	6	6	67	34	33
2	2021	2	Flamengo	71	38	21	8	9	69	36	33
3	2021	3	Palmeiras	66	38	20	6	12	58	43	15
4	2021	4	Fortaleza	58	38	17	7	14	44	45	-1
5	2021	5	Corinthians	57	38	15	12	11	40	36	4
6	2021	6	Red Bull Bragantino	56	38	14	14	10	55	46	9
7	2021	7	Fluminense	54	38	15	9	14	38	38	0
8	2021	8	América-MG	53	38	13	14	11	41	37	4
9	2021	9	Atlético-GO	53	38	13	14	11	33	36	-3
10	2021	10	Santos	50	38	12	14	12	35	40	-5
11	2021	11	Ceará	50	38	11	17	10	39	38	1
12	2021	12	Internacional	48	38	12	12	14	44	42	2
13	2021	13	São Paulo	48	38	11	15	12	31	39	-8
14	2021	14	Athletico-PR	47	38	13	8	17	41	45	-4
15	2021	15	Cuiabá	47	38	10	17	11	34	37	-3
16	2021	16	Juventude	46	38	11	13	14	36	44	-8
17	2021	17	Grêmio	43	38	12	7	19	44	51	-7
18	2021	18	Bahia	43	38	11	10	17	42	51	-9
19	2021	19	Sport	38	38	9	11	18	24	37	-13
20	2021	20	Chapecoense	15	38	1	12	25	27	67	-40
21	2022	1	Palmeiras	81	38	23	12	3	66	27	39
22	2022	2	Internacional	73	38	20	13	5	58	31	27
23	2022	3	Fluminense	70	38	21	7	10	63	41	22
24	2022	4	Corinthians	65	38	18	11	9	44	36	8
25	2022	5	Flamengo	62	38	18	8	12	60	39	21
26	2022	6	Athletico-PR	58	38	16	10	12	48	48	0
27	2022	7	Atlético-MG	58	38	15	13	10	45	37	8
28	2022	8	Fortaleza	55	38	15	10	13	46	39	7
29	2022	9	São Paulo	54	38	13	15	10	51	43	8
30	2022	10	América-MG	53	38	15	8	15	40	40	0
31	2022	11	Botafogo	53	38	15	8	15	41	43	-2
32	2022	12	Santos	47	38	12	11	15	44	41	3
33	2022	13	Goiás	46	38	11	13	14	44	53	-9
34	2022	14	Bragantino	44	38	11	11	16	49	59	-10
35	2022	15	Coritiba	42	38	12	6	20	39	60	-21
36	2022	16	Cuiabá	41	38	10	11	17	31	43	-12
37	2022	17	Ceará	37	38	7	16	15	34	37	-3
38	2022	18	Atlético-GO	36	38	9	9	20	39	63	-24
39	2022	19	Avaí	35	38	9	8	21	34	57	-23
40	2022	20	Juventude	22	38	3	13	22	29	69	-40
41	2023	1	Palmeiras	70	38	20	10	8	64	33	31
42	2023	2	Grêmio	68	38	21	5	12	63	56	7
43	2023	3	Atlético-MG	66	38	19	9	10	52	32	20
44	2023	4	Flamengo	66	38	19	9	10	56	42	14
45	2023	5	Botafogo	64	38	18	10	10	58	37	21
46	2023	6	Red Bull Bragantino	62	38	17	11	10	49	35	14
47	2023	7	Fluminense	56	38	16	8	14	51	47	4
48	2023	8	Athletico-PR	56	38	14	14	10	51	43	8
49	2023	9	Internacional	55	38	15	10	13	46	45	1
50	2023	10	Fortaleza	54	38	14	12	12	44	40	4
51	2023	11	São Paulo	53	38	14	11	13	40	38	2
52	2023	12	Cuiabá	51	38	14	9	15	39	47	-8
53	2023	13	Corinthians	50	38	12	14	12	47	48	-1
54	2023	14	Cruzeiro	47	38	11	14	13	35	32	3
55	2023	15	Vasco da Gama	45	38	12	9	17	41	51	-10
56	2023	16	Bahia	44	38	12	8	18	50	53	-3
57	2023	17	Santos	43	38	11	10	17	39	64	-25
58	2023	18	Goiás	38	38	9	11	18	36	53	-17
59	2023	19	Coritiba	30	38	8	6	24	41	73	-32
60	2023	20	América-MG	24	38	5	9	24	42	81	-39
81	2024	1	Botafogo	79	38	23	10	5	59	29	30
82	2024	2	Palmeiras	73	38	22	7	9	60	33	27
83	2024	3	Flamengo	70	38	20	10	8	61	42	19
84	2024	4	Fortaleza	68	38	19	11	8	53	39	14
85	2024	5	Internacional	65	38	18	11	9	53	36	17
86	2024	6	São Paulo	59	38	17	8	13	53	43	10
87	2024	7	Corinthians	56	38	15	11	12	54	45	9
88	2024	8	Bahia	53	38	15	8	15	49	49	0
89	2024	9	Cruzeiro	52	38	14	10	14	43	41	2
90	2024	10	Vasco da Gama	50	38	14	8	16	43	56	-13
91	2024	11	Vitória	47	38	13	8	17	45	52	-7
92	2024	12	Atlético-MG	47	38	11	14	13	47	54	-7
93	2024	13	Fluminense	46	38	12	10	16	33	39	-6
94	2024	14	Grêmio	45	38	12	9	17	44	50	-6
95	2024	15	Juventude	45	38	11	12	15	48	59	-11
96	2024	16	Red Bull Bragantino	44	38	10	14	14	44	48	-4
97	2024	17	Athletico-PR	42	38	11	9	18	40	46	-6
98	2024	18	Criciúma	38	38	9	11	18	42	61	-19
99	2024	19	Atlético-GO	30	38	7	9	22	29	58	-29
100	2024	20	Cuiabá	30	38	6	12	20	29	49	-20
101	2025	1	Flamengo	79	38	23	10	5	78	27	51
102	2025	2	Palmeiras	76	38	23	7	8	66	33	33
103	2025	3	Cruzeiro	70	38	19	13	6	55	31	24
104	2025	4	Mirassol	67	38	18	13	7	63	39	24
105	2025	5	Fluminense	64	38	19	7	12	50	39	11
106	2025	6	Botafogo	63	38	17	12	9	58	38	20
107	2025	7	Bahia	60	38	17	9	12	50	46	4
108	2025	8	São Paulo	51	38	14	9	15	43	47	-4
109	2025	9	Grêmio	49	38	13	10	15	47	50	-3
110	2025	10	Red Bull Bragantino	48	38	14	6	18	45	57	-12
111	2025	11	Atlético-MG	48	38	12	12	14	43	44	-1
112	2025	12	Santos	47	38	12	11	15	45	50	-5
113	2025	13	Corinthians	47	38	12	11	15	42	47	-5
114	2025	14	Vasco da Gama	45	38	13	6	19	55	60	-5
115	2025	15	Vitória	45	38	11	12	15	35	52	-17
116	2025	16	Internacional	44	38	11	11	16	44	57	-13
117	2025	17	Ceará	43	38	11	10	17	34	40	-6
118	2025	18	Fortaleza	43	38	11	10	17	43	58	-15
119	2025	19	Juventude	35	38	9	8	21	35	69	-34
120	2025	20	Sport	17	38	2	11	25	28	75	-47
\.


--
-- TOC entry 5028 (class 0 OID 0)
-- Dependencies: 221
-- Name: classificacao_atual_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.classificacao_atual_id_seq', 40, true);


--
-- TOC entry 5029 (class 0 OID 0)
-- Dependencies: 219
-- Name: historico_brasileirao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.historico_brasileirao_id_seq', 120, true);


--
-- TOC entry 4869 (class 2606 OID 16560)
-- Name: classificacao_atual classificacao_atual_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classificacao_atual
    ADD CONSTRAINT classificacao_atual_pkey PRIMARY KEY (id);


--
-- TOC entry 4865 (class 2606 OID 16539)
-- Name: historico_brasileirao historico_brasileirao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historico_brasileirao
    ADD CONSTRAINT historico_brasileirao_pkey PRIMARY KEY (id);


--
-- TOC entry 4867 (class 2606 OID 16541)
-- Name: historico_brasileirao temporada_posicao_unica; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historico_brasileirao
    ADD CONSTRAINT temporada_posicao_unica UNIQUE (temporada, posicao);


-- Completed on 2026-09-14 00:07:43

--
-- PostgreSQL database dump complete
--

\unrestrict 66syfwsMRZW7iWOxpJiYp3s7j0o6pHwDWeszVf97TdvveXJnbjxfNNxQaal7Bwf

