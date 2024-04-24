import React, { useState, useMemo, useEffect } from "react";
import PropTypes from "prop-types";
import cn from "classnames";
import countryList from "react-select-country-list";
import styles from "./index.module.scss";
import "react-phone-number-input/style.css";
import PhoneInput from "react-phone-number-input";
import Chatbot from "../../components/chatbot/Chatbot";

function ScrollToTop() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return null;
}

function DemandePartenariat(props) {
  const defaultCountryCode = "DZ"; // Algeria country code
  const [country, setCountry] = useState(defaultCountryCode);
  const countryOptions = useMemo(() => countryList().getData(), []);

  const [phoneNumber, setPhoneNumber] = useState("");

  const handleCountryChange = (event) => {
    setCountry(event.target.value);
  };

  const handlePhoneChange = (value) => {
    setPhoneNumber(value);
  };

  const [tailleValue, setTailleValue] = useState("");

  const handleTailleChange = (event) => {
    setTailleValue(event.target.value);
  };
  const tailleOptions = [
    { label: "Moins de 10 personnes", value: "Moins de 10 personnes" },
    { label: "10 à 50 personnes", value: "10 à 50 personnes" },
    { label: "50 à 100 personnes", value: "50 à 100 personnes" },
    { label: "Plus de 100 personnes", value: "Plus de 100 personnes" },
  ];

  return (
    <div className={cn(styles.root, props.className, "demande-partenariat")}>
      <ScrollToTop />
      <Chatbot />
      <div className={styles.rect1} />
      <div className={styles.rectBlanc} />
      <img
        className={styles.image}
        src={"/assets/fa6ac9119371246826f9dcc1db7c7c0c.png"}
        alt="alt text"
      />
      <img
        className={styles.cover}
        src={"/assets/2ff91be7ff07fa23f5bb6f2678e3e9de.png"}
        alt="alt text"
      />
      <div className={styles.rect3} />
      <img
        className={styles.image1}
        src={"/assets/19bddda9a0a00c68e91c5e681f2fac67.png"}
        alt="alt text"
      />
      <div className={styles.rect4} />
      <div className={styles.text}>SDN</div>
      <div className={styles.text1}>E-Plateforme</div>
      <div className={styles.text2}>Actualités</div>
      <div className={styles.text3}>{`Ecole & staff`}</div>
      <div className={styles.text4}>Evenements</div>
      <div className={styles.text5}>Alumnis</div>
      <div className={styles.text6}>MyESI</div>

      <img
        className={styles.image2}
        src={"/assets/35535b9121925ff92c4729aa4df8acf1.png"}
        alt="alt text"
      />
      <img
        className={styles.image3}
        src={"/assets/90c3a65f5858f9dc479a45c7d57a543b.png"}
        alt="alt text"
      />
      <div className={styles.text7}>Français</div>
      <img
        className={styles.image4}
        src={"/assets/cc2504418786f2711f9593f3a9a7d2cd.png"}
        alt="alt text"
      />
      <img
        className={styles.image5}
        src={"/assets/2d5d82a9400afa1df204663b627dbf3e.png"}
        alt="alt text"
      />
      <img
        className={styles.image6}
        src={"/assets/0ed15c190e16f7fd26013bf79b2ff8cf.png"}
        alt="alt text"
      />
      <img
        className={styles.image7}
        src={"/assets/23ff70017dd90eb3bcdb62ff83f1fcf9.png"}
        alt="alt text"
      />
      <img
        className={styles.image8}
        src={"/assets/5b148828fa2190c7edf3daf6dc75bdfc.png"}
        alt="alt text"
      />
      <img
        className={styles.image13}
        src={"/assets/955c4e940b85d44faba2746fe0a33df8.png"}
        alt="alt text"
      />
      <img
        className={styles.image14}
        src={"/assets/155314d6f587f1b54286cd0197b228b1.png"}
        alt="alt text"
      />
      <img
        className={styles.image15}
        src={"/assets/c173676257d6995eaec68a569df84d56.png"}
        alt="alt text"
      />
      <img
        className={styles.image16}
        src={"/assets/1973c28649ee9db57cc4a17ef741310e.png"}
        alt="alt text"
      />
      <img
        className={styles.image17}
        src={"/assets/75b46780da2ee962f468c6df9cdb01d0.png"}
        alt="alt text"
      />

      <div className={styles.wrapper}>
        <img
          className={styles.image18}
          src={"/assets/3640f2ab319c36d1ef8046e55b264c2f.png"}
          alt="alt text"
        />
        <img
          className={styles.image181}
          src={"/assets/c4ceed0a163602af7415992b6d090cec.png"}
          alt="alt text"
        />
        <img
          className={styles.image182}
          src={"/assets/9aa94fd605d94e1418e6f78ffc0c5fb4.png"}
          alt="alt text"
        />
        <img
          className={styles.image19}
          src={"/assets/ba9ae6607ea9c6d9beb2a2bd0e06f03d.png"}
          alt="alt text"
        />
        <img
          className={styles.image20}
          src={"/assets/55ac65233899c7f8b893b842612b882f.png"}
          alt="alt text"
        />
        <img
          className={styles.image21}
          src={"/assets/3645c70652970328341dd93841548972.png"}
          alt="alt text"
        />
        <img
          className={styles.image211}
          src={"/assets/e65774c5184e33b8cfc463062db19e95.png"}
          alt="alt text"
        />
        <img
          className={styles.image22}
          src={"/assets/3cc5267f24d4e5fac606497c1b856a06.png"}
          alt="alt text"
        />
        <img
          className={styles.image23}
          src={"/assets/7b619a80ab2faf0714ae338561035af0.png"}
          alt="alt text"
        />
        <img
          className={styles.image231}
          src={"/assets/6248bc0015d9ccc4402ab241cd0975f6.png"}
          alt="alt text"
        />
        <div className={styles.rect8} />
        <img
          className={styles.image24}
          src={"/assets/abdf44349846beec6b8a3b0a52179540.png"}
          alt="alt text"
        />
        <img
          className={styles.image221}
          src={"/assets/829fa4b26204825a762914d9a83c346f.png"}
          alt="alt text"
        />
        <img
          className={styles.image241}
          src={"/assets/4f94590be40902a2bf9e0445779c7ccd.png"}
          alt="alt text"
        />
        <img
          className={styles.image25}
          src={"/assets/94825010e7ae467bdea45cc5b7a276b5.png"}
          alt="alt text"
        />
        <img
          className={styles.image251}
          src={"/assets/a1f50f7e466fcdd976480d63a1082a6b.png"}
          alt="alt text"
        />
        <img
          className={styles.image242}
          src={"/assets/7b97a593e603d114afa17c59069173db.png"}
          alt="alt text"
        />
        <img
          className={styles.image222}
          src={"/assets/815d59e04575e17d387ac165d841df92.png"}
          alt="alt text"
        />
        <img
          className={styles.image252}
          src={"/assets/1656c9ff71f2cf2db35999ad65b79d22.png"}
          alt="alt text"
        />
        <img
          className={styles.image243}
          src={"/assets/3d629b1856187a54b1493869bec27ce4.png"}
          alt="alt text"
        />
        <img
          className={styles.image253}
          src={"/assets/950e87265fcb00a84d16f464f87cd318.png"}
          alt="alt text"
        />
        <img
          className={styles.image254}
          src={"/assets/f7c23a69900f1768d02aedf9956a7119.png"}
          alt="alt text"
        />
        <img
          className={styles.image232}
          src={"/assets/ab1fa5643da3ab3daa75eeb0324dd826.png"}
          alt="alt text"
        />
        <img
          className={styles.image26}
          src={"/assets/d6da573e220ba48f940ffa310a51a072.png"}
          alt="alt text"
        />
        <img
          className={styles.image27}
          src={"/assets/f761447dab672e0d377b1a71f78250c7.png"}
          alt="alt text"
        />
        <div className={styles.rect9} />
        <img
          className={styles.image261}
          src={"/assets/6729ef65b0f41e9ee4a33f9ea8fdd741.png"}
          alt="alt text"
        />
        <img
          className={styles.image271}
          src={"/assets/3063e0ec0eaccd75ce06d5fa5928b8b9.png"}
          alt="alt text"
        />
        <img
          className={styles.image262}
          src={"/assets/4804922fb862e187046a39b6456656f1.png"}
          alt="alt text"
        />
        <img
          className={styles.image272}
          src={"/assets/0e8a342bc47f6eef4520f9802038f956.png"}
          alt="alt text"
        />
        <div className={styles.rect91} />
        <img
          className={styles.image263}
          src={"/assets/f2c7b8b99f1a99591aeb692a935b9a38.png"}
          alt="alt text"
        />
        <img
          className={styles.image28}
          src={"/assets/8835f3dff3abd1f8896b610bdc6b60d0.png"}
          alt="alt text"
        />
      </div>
      <img
        className={styles.image29}
        src={"/assets/37d66477ea54eacefa0ec66d0d43a240.png"}
        alt="alt text"
      />
      <img
        className={styles.image30}
        src={"/assets/13fa3e147606018ff2a638149285a2dc.png"}
        alt="alt text"
      />
      <img
        className={styles.image31}
        src={"/assets/2cdae197e42ac67f869fc876aa169a53.png"}
        alt="alt text"
      />
      <img
        className={styles.image32}
        src={"/assets/67c6542b643533e647cf838b081f455e.png"}
        alt="alt text"
      />
      <img
        className={styles.image33}
        src={"/assets/a12a185a18bbe0ff6fe86a26ccba6127.png"}
        alt="alt text"
      />
      <img
        className={styles.image34}
        src={"/assets/ca020455e318c447fb1c05a22181bb20.png"}
        alt="alt text"
      />
      <img
        className={styles.image35}
        src={"/assets/ad702051d3376067762a8be06c74483a.png"}
        alt="alt text"
      />
      <h2 className={styles.medium_title}>Notre réseau de partenaires</h2>

      <div className={styles.box}>
        <div className={styles.rect10} />
        <h4 className={styles.highlight1}>Simulation des devis</h4>
        <h5 className={styles.highlight2}>
          Personnalisez votre experience et simplifiez vos demandes de devis et
          simulez les coûts en quelques clics avec notre simulateur de devis !
        </h5>
      </div>
      <div className={styles.box1}>
        <div className={styles.rect10} />
        <h4 className={styles.highlight11}>
          Flexibilité et Engagement Améliorés
        </h4>
        <h5
          className={styles.highlight21}
        >{`Profitez d'une expérience de formation sur mesure avec la possibilité de suivre les sessions en cours à distance. Accédez aux ressources pédagogiques en ligne et aux documents administratifs à tout moment`}</h5>
      </div>
      <div className={styles.box2}>
        <div className={styles.rect10} />
        <h4 className={styles.highlight12}>
          Accessibilité et Transparence Renforcées
        </h4>
        <h5 className={styles.highlight2}>
          Accédez instantanément à notre gamme complète de formations continues
          grâce à une consultation en ligne des catalogues.
        </h5>
      </div>
      <div className={styles.rect12} />

      <div className={styles.centeredDiv1}>
        <h3 className={styles.subtitle_box}>
          <span className={styles.subtitle}>
            <span className={styles.subtitle_span0}>
              {`Joignez-vous à l'Élan de l'Excellence : `}
              <br />
              Devenez{" "}
            </span>
            <span className={styles.subtitle_span1}>Notre Partenaire!</span>
          </span>
        </h3>
        <h3 className={styles.subtitle1}>
          {`Expertise, Collaboration & `}
          <br />
          Innovation
        </h3>
        <h5 className={styles.textDescr}>
          Plongez dans un monde d'opportunités sans limites en devenant
          partenaire de l'ESI. Notre engagement envers l'excellence scientifique
          et économique se traduit par des alliances stratégiques dynamiques
          <br />
          {`l'avenir ensemble.`}
        </h5>

        <div className={styles.formContainer}>
          <div className={styles.rect13} />
          <img
            className={styles.cover1}
            src={"/assets/497044dd465bb37b6c038e3797fc55df.png"}
            alt="alt text"
          />
          <h5 className={styles.highlight3}>Soumettre</h5>
          <div className={styles.rect14} />
          <h4 className={styles.highlight4}>Rejoignez-nous</h4>
          <div className={styles.text21_box}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Email Professionnel </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box1}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Prenom </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box2}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Profession </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text22}>URL du site web</div>
          <div className={styles.text21_box3}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>
                Taille de l’organisme{" "}
              </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box4}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Nom de l’organisme </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box5}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Numero de telephone </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box6}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Pays </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>
          <div className={styles.text21_box7}>
            <span className={styles.text21}>
              <span className={styles.text21_span0}>Nom </span>
              <span className={styles.text21_span1}>*</span>
            </span>
          </div>

          <div className={styles.rect15}>
            <input className={styles.transparentInput} type="email" />
          </div>

          <div className={styles.rect16}>
            <input className={styles.transparentInput} type="text" />
          </div>

          <div className={styles.rect161}>
            <input className={styles.transparentInput} type="text" />
          </div>

          <div className={styles.rect162}>
            <input className={styles.transparentInput} type="text" />
          </div>

          <div className={styles.rect163}>
            <select
              className={styles.transparentInput}
              value={tailleValue}
              onChange={handleTailleChange}
            >
              <option value=""></option>
              {tailleOptions.map((option, index) => (
                <option key={index} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          <PhoneInput
            placeholder="Entrez votre numero"
            value={phoneNumber}
            onChange={handlePhoneChange}
            className={`${styles.transparentInput} ${styles.rect151}`}
          />

          <div className={styles.rect152}>
            <input className={styles.transparentInput} type="text" />
          </div>

          <div className={styles.rect164}>
            <input className={styles.transparentInput} type="text" />
          </div>
          <div className={styles.rect165}>
            <select
              className={styles.countrySelector}
              onChange={handleCountryChange}
              value={country}
            >
              {countryOptions.map((option, index) => (
                <option key={index} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        <img
          className={styles.image36}
          src={"/assets/c39fb1514750b48887bc7e72dbb9e61f.png"}
          alt="alt text"
        />
        <img
          className={styles.image37}
          src={"/assets/abef9052c9f911d0dfc6a8f9e1df3932.png"}
          alt="alt text"
        />
        <h5 className={styles.highlight5}>
          Que vous cherchiez une expertise pointue, des <br />
          collaborations de recherche stimulantes ou des <br />
          solutions de formation continue innovantes, notre <br />
          équipe dévouée est prête à transformer vos <br />
          aspirations en réalité. Rejoignez-nous pour façonner
          <br />
          {`l'avenir ensemble.`}
        </h5>
      </div>
    </div>
  );
}

DemandePartenariat.propTypes = {
  className: PropTypes.string,
};

export default DemandePartenariat;
