# django
<a target="_blank" href="https://portfolio.kevinlamarque.fr/blog/app/django/">Portfolio-blog-django</a>
# Partie 1 : Initiation
A travers différentes parties , construisons un blog permettant la gestion des posts, des articles ou de commentaires
Pré-requis
Connaître les bases de Python
Etre à l'aise avec les fonctions, connaître la programmation orientée objet serait un plus
Comprendre les fonctionnements de base du Web
Etre curieux

<ul>
<li><strong>Partie 1 :&nbsp;</strong>
<ul>
<li><a href="#create_app">1.1 Cr&eacute;ation de l'application</a></li>
<li><a href="#update_app">1.2 Modification de l'application</a></li>
<li><a href="#update_setting">1.3 Modification du fichier settings.py</a></li>
<li><a href="#static_files">1.4 Gestion des fichiers statiques </a></li>
</ul>
</li>
<li><strong>Partie 2 :&nbsp;</strong>
<ul>
<li><a href="#create_models">2.1 Cr&eacute;ation des models</a></li>
<li><a href="#app_migrate">2.2 Applications des migrations </a></li>
<li><a href="#model_admin">&nbsp;2.3 Afficher les mod&egrave;les dans l'administration</a></li>
<li><a href="#create_post">2.4 Cr&eacute;ation d'un post </a></li>
<li><a href="#update_model_media">2.5 Modification mod&egrave;le Media</a></li>
</ul>
</li>
<li><strong>Partie 3 :&nbsp;</strong>
<ul>
<li><a href="#create_views">3.1&nbsp;</a><a href="#create_views">r&eacute;ation des vues</a></li>
<li><span style="color: #000000;"><a href="#update_urls">3.2 Modification des URLS </a></span></li>
</ul>
</li>
<li><strong><span style="color: #000000;">Partie 4 :</span></strong>
<ul>
<li><span style="color: #000000;"><a href="#base_html">4.1 Fichier base.html</a></span></li>
<li><span style="color: #000000;"><a href="#nav_">4.2 Fichier nav.html</a></span></li>
<li><span style="color: #000000;"><a href="#gabarit">4.3 Cr&eacute;ation des gabarits&nbsp;</a></span>
<ul>
<li><span ><a href="#posts_gabarit">4.3.1 Cr&eacute;ation du gabarit post </a></span></li>
<li><span><a href="#gabarit_image">4.3.2 Cr&eacute;ation du gabarit image</a></span></li>
</ul>
</li>
</ul>
</li>
<li><span><a href="#sources">Les sources</a></span></li>
</ul>

# Partie 2 Initiation partie 2 
<ul>
<li><strong>Partie 1 :</strong>
<ul>
<li><a href="#add_style">1.1 Ajout de style</a></li>
<li><a href="#add_article">1.2 Ajout du mod&egrave;le Article</a></li>
</ul>
</li>
<li><strong>Partie 1.2 :</strong>
<ul>
<li><a href="#add_venv">1.2.1 Installation de l'environnement virtuel</a></li>
<li><a href="#add_sql"> 1.2.2 Changement de moteur SQL</a></li>
</ul>
</li>
<li><strong>Partie 2:&nbsp;</strong>
<ul>
<li><a href="#add_tinymce">2.1 Installation Tinymce</a></li>
<li><a href="#update_article">2.2 Modification mod&egrave;le Article</a></li>
</ul>
</li>
<li><strong>Partie 3 :&nbsp;</strong>
<ul>
<li><a href="#search_cat">3.1 Gestion des cat&eacute;gories </a>
<ul>
<li><a href="#create_vue_cat">3.1.1 Cr&eacute;ation de la vue</a></li>
<li><a href="#update_url_cat">3.1.2 Modification de l'URL</a></li>
</ul>
</li>
<li><a href="#gestion_comment">3.2 Gestion des commentaires</a>
<ul>
<li><a href="#create_model_comment">3.2.1 Cr&eacute;ation de la classe Comment</a></li>
<li><a href="#create_form">3.2.2 Cr&eacute;ation du formulaire</a></li>
<li><a href="#update_view_article">3.3.3 Modification de la vue Article</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#sources">Sources</a></li>
</ul>

