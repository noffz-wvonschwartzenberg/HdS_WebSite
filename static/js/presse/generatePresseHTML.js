import {presse} from './presse.js';

export function generatePresseHTML()
{
    let presseHTML = '';
    presse.forEach((press) => {
        presseHTML += `
        <div class="article-line"> 
            <div class="article-column">
                <img src="${press.Logo}" alt="${press.LogoText}" class="image-logo">
                <p class="article-date">${press.ArticleDate}</p>
            </div>
            <a class="article-title" href="${press.ArticleLink}">${press.ArticleTitle}</a>
        </div>`;
    });

    return presseHTML;
}

