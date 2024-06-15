PGDMP  7    3        	        |            project    16.3    16.3 ?    0           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            1           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            2           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            3           1262    32768    project    DATABASE     �   CREATE DATABASE project WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Indonesian_Indonesia.1252';
    DROP DATABASE project;
                postgres    false            �            1259    155802    admin    TABLE     �   CREATE TABLE public.admin (
    id_admin integer NOT NULL,
    no_induk_pegawai character varying(16) NOT NULL,
    nama_admin character varying(32) NOT NULL,
    password_pegawai character varying(16) NOT NULL,
    id_cabang integer DEFAULT 3102
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    155801    admin_id_admin_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_id_admin_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.admin_id_admin_seq;
       public          postgres    false    218            4           0    0    admin_id_admin_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.admin_id_admin_seq OWNED BY public.admin.id_admin;
          public          postgres    false    217            �            1259    180407    barang    TABLE     9  CREATE TABLE public.barang (
    id_barang integer NOT NULL,
    nama_barang character varying(32) NOT NULL,
    jenis_barang character varying(32) NOT NULL,
    merk_barang character varying(32) NOT NULL,
    stok_barang integer NOT NULL,
    harga_barang integer NOT NULL,
    id_cabang integer DEFAULT 3102
);
    DROP TABLE public.barang;
       public         heap    postgres    false            �            1259    180406    barang_id_barang_seq    SEQUENCE     �   CREATE SEQUENCE public.barang_id_barang_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.barang_id_barang_seq;
       public          postgres    false    224            5           0    0    barang_id_barang_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.barang_id_barang_seq OWNED BY public.barang.id_barang;
          public          postgres    false    223            �            1259    114800    cabang    TABLE     �   CREATE TABLE public.cabang (
    id_cabang integer NOT NULL,
    nama_cabang character varying(64) NOT NULL,
    alamat_cabang character varying(128) NOT NULL,
    no_telfon character varying(16) NOT NULL
);
    DROP TABLE public.cabang;
       public         heap    postgres    false            �            1259    164012    data_pelanggan    TABLE     �   CREATE TABLE public.data_pelanggan (
    id_pelanggan integer NOT NULL,
    nama_pelanggan character varying(32) NOT NULL,
    alamat_pelanggan character varying(128) NOT NULL,
    no_telfon character varying(16) NOT NULL
);
 "   DROP TABLE public.data_pelanggan;
       public         heap    postgres    false            �            1259    164011    data_pelanggan_id_pelanggan_seq    SEQUENCE     �   CREATE SEQUENCE public.data_pelanggan_id_pelanggan_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.data_pelanggan_id_pelanggan_seq;
       public          postgres    false    222            6           0    0    data_pelanggan_id_pelanggan_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.data_pelanggan_id_pelanggan_seq OWNED BY public.data_pelanggan.id_pelanggan;
          public          postgres    false    221            �            1259    180424    detail_pesanan    TABLE     r  CREATE TABLE public.detail_pesanan (
    id_pesanan integer NOT NULL,
    tanggal date NOT NULL,
    jumlah_barang integer NOT NULL,
    biaya_pasang integer DEFAULT 200000,
    status_pembayaran character varying(16) DEFAULT 'BELUM LUNAS'::character varying NOT NULL,
    id_barang integer NOT NULL,
    id_pelanggan integer NOT NULL,
    id_metode integer NOT NULL
);
 "   DROP TABLE public.detail_pesanan;
       public         heap    postgres    false            �            1259    180421    detail_pesanan_id_barang_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_pesanan_id_barang_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.detail_pesanan_id_barang_seq;
       public          postgres    false    229            7           0    0    detail_pesanan_id_barang_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.detail_pesanan_id_barang_seq OWNED BY public.detail_pesanan.id_barang;
          public          postgres    false    226            �            1259    180423    detail_pesanan_id_metode_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_pesanan_id_metode_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.detail_pesanan_id_metode_seq;
       public          postgres    false    229            8           0    0    detail_pesanan_id_metode_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.detail_pesanan_id_metode_seq OWNED BY public.detail_pesanan.id_metode;
          public          postgres    false    228            �            1259    180422    detail_pesanan_id_pelanggan_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_pesanan_id_pelanggan_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.detail_pesanan_id_pelanggan_seq;
       public          postgres    false    229            9           0    0    detail_pesanan_id_pelanggan_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.detail_pesanan_id_pelanggan_seq OWNED BY public.detail_pesanan.id_pelanggan;
          public          postgres    false    227            �            1259    180420    detail_pesanan_id_pesanan_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_pesanan_id_pesanan_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.detail_pesanan_id_pesanan_seq;
       public          postgres    false    229            :           0    0    detail_pesanan_id_pesanan_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.detail_pesanan_id_pesanan_seq OWNED BY public.detail_pesanan.id_pesanan;
          public          postgres    false    225            �            1259    114830    metode_pembayaran    TABLE        CREATE TABLE public.metode_pembayaran (
    id_metode integer NOT NULL,
    media_pembayaran character varying(32) NOT NULL
);
 %   DROP TABLE public.metode_pembayaran;
       public         heap    postgres    false            �            1259    155854    teknisi    TABLE     �   CREATE TABLE public.teknisi (
    id_teknisi integer NOT NULL,
    nama_teknisi character varying(32) NOT NULL,
    no_telfon character varying(16) NOT NULL,
    id_cabang integer DEFAULT 3102
);
    DROP TABLE public.teknisi;
       public         heap    postgres    false            �            1259    155853    teknisi_id_teknisi_seq    SEQUENCE     �   CREATE SEQUENCE public.teknisi_id_teknisi_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.teknisi_id_teknisi_seq;
       public          postgres    false    220            ;           0    0    teknisi_id_teknisi_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.teknisi_id_teknisi_seq OWNED BY public.teknisi.id_teknisi;
          public          postgres    false    219            o           2604    155805    admin id_admin    DEFAULT     p   ALTER TABLE ONLY public.admin ALTER COLUMN id_admin SET DEFAULT nextval('public.admin_id_admin_seq'::regclass);
 =   ALTER TABLE public.admin ALTER COLUMN id_admin DROP DEFAULT;
       public          postgres    false    217    218    218            t           2604    180410    barang id_barang    DEFAULT     t   ALTER TABLE ONLY public.barang ALTER COLUMN id_barang SET DEFAULT nextval('public.barang_id_barang_seq'::regclass);
 ?   ALTER TABLE public.barang ALTER COLUMN id_barang DROP DEFAULT;
       public          postgres    false    224    223    224            s           2604    164015    data_pelanggan id_pelanggan    DEFAULT     �   ALTER TABLE ONLY public.data_pelanggan ALTER COLUMN id_pelanggan SET DEFAULT nextval('public.data_pelanggan_id_pelanggan_seq'::regclass);
 J   ALTER TABLE public.data_pelanggan ALTER COLUMN id_pelanggan DROP DEFAULT;
       public          postgres    false    222    221    222            v           2604    180427    detail_pesanan id_pesanan    DEFAULT     �   ALTER TABLE ONLY public.detail_pesanan ALTER COLUMN id_pesanan SET DEFAULT nextval('public.detail_pesanan_id_pesanan_seq'::regclass);
 H   ALTER TABLE public.detail_pesanan ALTER COLUMN id_pesanan DROP DEFAULT;
       public          postgres    false    225    229    229            y           2604    180430    detail_pesanan id_barang    DEFAULT     �   ALTER TABLE ONLY public.detail_pesanan ALTER COLUMN id_barang SET DEFAULT nextval('public.detail_pesanan_id_barang_seq'::regclass);
 G   ALTER TABLE public.detail_pesanan ALTER COLUMN id_barang DROP DEFAULT;
       public          postgres    false    229    226    229            z           2604    180431    detail_pesanan id_pelanggan    DEFAULT     �   ALTER TABLE ONLY public.detail_pesanan ALTER COLUMN id_pelanggan SET DEFAULT nextval('public.detail_pesanan_id_pelanggan_seq'::regclass);
 J   ALTER TABLE public.detail_pesanan ALTER COLUMN id_pelanggan DROP DEFAULT;
       public          postgres    false    229    227    229            {           2604    180432    detail_pesanan id_metode    DEFAULT     �   ALTER TABLE ONLY public.detail_pesanan ALTER COLUMN id_metode SET DEFAULT nextval('public.detail_pesanan_id_metode_seq'::regclass);
 G   ALTER TABLE public.detail_pesanan ALTER COLUMN id_metode DROP DEFAULT;
       public          postgres    false    229    228    229            q           2604    155857    teknisi id_teknisi    DEFAULT     x   ALTER TABLE ONLY public.teknisi ALTER COLUMN id_teknisi SET DEFAULT nextval('public.teknisi_id_teknisi_seq'::regclass);
 A   ALTER TABLE public.teknisi ALTER COLUMN id_teknisi DROP DEFAULT;
       public          postgres    false    220    219    220            "          0    155802    admin 
   TABLE DATA           d   COPY public.admin (id_admin, no_induk_pegawai, nama_admin, password_pegawai, id_cabang) FROM stdin;
    public          postgres    false    218   �L       (          0    180407    barang 
   TABLE DATA           y   COPY public.barang (id_barang, nama_barang, jenis_barang, merk_barang, stok_barang, harga_barang, id_cabang) FROM stdin;
    public          postgres    false    224   �L                 0    114800    cabang 
   TABLE DATA           R   COPY public.cabang (id_cabang, nama_cabang, alamat_cabang, no_telfon) FROM stdin;
    public          postgres    false    215   �M       &          0    164012    data_pelanggan 
   TABLE DATA           c   COPY public.data_pelanggan (id_pelanggan, nama_pelanggan, alamat_pelanggan, no_telfon) FROM stdin;
    public          postgres    false    222   N       -          0    180424    detail_pesanan 
   TABLE DATA           �   COPY public.detail_pesanan (id_pesanan, tanggal, jumlah_barang, biaya_pasang, status_pembayaran, id_barang, id_pelanggan, id_metode) FROM stdin;
    public          postgres    false    229   �N                  0    114830    metode_pembayaran 
   TABLE DATA           H   COPY public.metode_pembayaran (id_metode, media_pembayaran) FROM stdin;
    public          postgres    false    216   8O       $          0    155854    teknisi 
   TABLE DATA           Q   COPY public.teknisi (id_teknisi, nama_teknisi, no_telfon, id_cabang) FROM stdin;
    public          postgres    false    220   |O       <           0    0    admin_id_admin_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.admin_id_admin_seq', 1, false);
          public          postgres    false    217            =           0    0    barang_id_barang_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.barang_id_barang_seq', 5, true);
          public          postgres    false    223            >           0    0    data_pelanggan_id_pelanggan_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.data_pelanggan_id_pelanggan_seq', 7, true);
          public          postgres    false    221            ?           0    0    detail_pesanan_id_barang_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.detail_pesanan_id_barang_seq', 1, false);
          public          postgres    false    226            @           0    0    detail_pesanan_id_metode_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.detail_pesanan_id_metode_seq', 1, false);
          public          postgres    false    228            A           0    0    detail_pesanan_id_pelanggan_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.detail_pesanan_id_pelanggan_seq', 1, false);
          public          postgres    false    227            B           0    0    detail_pesanan_id_pesanan_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.detail_pesanan_id_pesanan_seq', 1, false);
          public          postgres    false    225            C           0    0    teknisi_id_teknisi_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.teknisi_id_teknisi_seq', 5, true);
          public          postgres    false    219            �           2606    155808    admin admin_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id_admin);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    218            �           2606    180413    barang barang_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.barang
    ADD CONSTRAINT barang_pkey PRIMARY KEY (id_barang);
 <   ALTER TABLE ONLY public.barang DROP CONSTRAINT barang_pkey;
       public            postgres    false    224            }           2606    114804    cabang cabang_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.cabang
    ADD CONSTRAINT cabang_pkey PRIMARY KEY (id_cabang);
 <   ALTER TABLE ONLY public.cabang DROP CONSTRAINT cabang_pkey;
       public            postgres    false    215            �           2606    164018 "   data_pelanggan data_pelanggan_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.data_pelanggan
    ADD CONSTRAINT data_pelanggan_pkey PRIMARY KEY (id_pelanggan);
 L   ALTER TABLE ONLY public.data_pelanggan DROP CONSTRAINT data_pelanggan_pkey;
       public            postgres    false    222            �           2606    180434 "   detail_pesanan detail_pesanan_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.detail_pesanan
    ADD CONSTRAINT detail_pesanan_pkey PRIMARY KEY (id_pesanan);
 L   ALTER TABLE ONLY public.detail_pesanan DROP CONSTRAINT detail_pesanan_pkey;
       public            postgres    false    229                       2606    114834 (   metode_pembayaran metode_pembayaran_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.metode_pembayaran
    ADD CONSTRAINT metode_pembayaran_pkey PRIMARY KEY (id_metode);
 R   ALTER TABLE ONLY public.metode_pembayaran DROP CONSTRAINT metode_pembayaran_pkey;
       public            postgres    false    216            �           2606    155860    teknisi teknisi_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.teknisi
    ADD CONSTRAINT teknisi_pkey PRIMARY KEY (id_teknisi);
 >   ALTER TABLE ONLY public.teknisi DROP CONSTRAINT teknisi_pkey;
       public            postgres    false    220            �           2606    180435    detail_pesanan fk_barang    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_pesanan
    ADD CONSTRAINT fk_barang FOREIGN KEY (id_barang) REFERENCES public.barang(id_barang) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.detail_pesanan DROP CONSTRAINT fk_barang;
       public          postgres    false    4743    224    229            �           2606    155809    admin fk_cabang    FK CONSTRAINT     �   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT fk_cabang FOREIGN KEY (id_cabang) REFERENCES public.cabang(id_cabang) ON DELETE CASCADE;
 9   ALTER TABLE ONLY public.admin DROP CONSTRAINT fk_cabang;
       public          postgres    false    218    215    4733            �           2606    155861    teknisi fk_cabang    FK CONSTRAINT     �   ALTER TABLE ONLY public.teknisi
    ADD CONSTRAINT fk_cabang FOREIGN KEY (id_cabang) REFERENCES public.cabang(id_cabang) ON DELETE CASCADE;
 ;   ALTER TABLE ONLY public.teknisi DROP CONSTRAINT fk_cabang;
       public          postgres    false    215    4733    220            �           2606    180414    barang fk_cabang    FK CONSTRAINT     �   ALTER TABLE ONLY public.barang
    ADD CONSTRAINT fk_cabang FOREIGN KEY (id_cabang) REFERENCES public.cabang(id_cabang) ON DELETE CASCADE;
 :   ALTER TABLE ONLY public.barang DROP CONSTRAINT fk_cabang;
       public          postgres    false    224    215    4733            �           2606    180440     detail_pesanan fk_data_pelanggan    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_pesanan
    ADD CONSTRAINT fk_data_pelanggan FOREIGN KEY (id_pelanggan) REFERENCES public.data_pelanggan(id_pelanggan) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.detail_pesanan DROP CONSTRAINT fk_data_pelanggan;
       public          postgres    false    4741    222    229            �           2606    180445 #   detail_pesanan fk_metode_pembayaran    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_pesanan
    ADD CONSTRAINT fk_metode_pembayaran FOREIGN KEY (id_metode) REFERENCES public.metode_pembayaran(id_metode) ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.detail_pesanan DROP CONSTRAINT fk_metode_pembayaran;
       public          postgres    false    4735    216    229            "   6   x�340�465�4202�t��MLQJL��w
�44261�4640����� �:
0      (   �   x�]�A�@�ϳ�E�w7;*�d
�TH0'�F���+����=���ܴ�*�""E��2���4< Ġ�@r>HP��`�޲3;Y/�'ؒI ]�ۮl��� �n1��d��M���JW�������<5��c��0�񞏯����)�X�5�<         o   x�3640�I����U�NM��+N,�T�J�MJ-����S�I-�J�KQ.-(J,(�W���37�A(1���� -�v �X����[Z�`fahd�i`llhllnni����� 1&r      &   �   x�]��j�0��� ���v�iOu��%�5�{�D��W�-��|�(�1����D6.-�� �OhA��"ҵ�ѭ��t����A)�dg{��f{�DW�tu[���b^�.x��-�"�b!��(��SR���f�q���0��=�=ǒ�[߸�'&��� �`���ҒK6��a�z�[�dJ��1�%�"(U'Xkt�v��r�� �NJ      -   3   x�340�4202�50�5��4r@����'�W�'��1$�ij`����� ��          4   x�350�tJ��V�M�K�,��250�8y9�P��c���������� ���      $   k   x�-��
1��s�0�L��W}ף��A|�m���c�e��@=<�A�T��S������a����[?]r�pMYd�ӹޟ�K�<�B���K�zW�0~b�끙w~�V     