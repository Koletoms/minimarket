var mix = {
    methods: {
        setTag (id) {
            this.topTags = this.topTags.map(tag => {
                return  tag.id === id ? { ...tag, selected: !tag.selected } : tag
            })
            this.getCatalogs()
        },
        setSort (id) {
            if (this.selectedSort?.id === id) {
                this.selectedSort.selected = (this.selectedSort.selected === 'dec' ? 'inc' : 'dec')
            }
            else {
                if (this.selectedSort) { this.selectedSort = null}
                this.selectedSort = this.sortRules.find(sort => sort.id === id)
                this.selectedSort = { ...this.selectedSort, selected: 'inc'}
            }
            this.getCatalogs()
        },
        getTags() {
            this.getData('/api/tags', { category: this.category })
            .then(data => this.topTags = data.map(tag => ({
                ...tag,
                selected: false
            })))
            .catch(() => {
                this.topTags = []
                console.warn('Ошибка получения тегов')
            })
        },
        getCatalogs(page) {
            if(typeof page === "undefined") { page = 1 }
            const PAGE_LIMIT = 3
            const tags = this.topTags.filter(tag => !!tag.selected).map(tag => tag.id)
            const sort_direction = (this.selectedSort ? this.selectedSort.selected : null) === 'dec' ? '-': '' // Изврат чтобы в CSS работа нормально
            const sort_name = this.selectedSort ? this.selectedSort.id : null
            const free_delivery = this.filter_free_delivery === false ? null : true
            const catalog_id = location.pathname.startsWith('/catalog/')
            ? Number(location.pathname.replace('/catalog/', ''))
            : null
            this.getData("/api/catalog/", {
                page: page,
                category: catalog_id === 0 ? null : catalog_id,
                ordering: sort_direction + sort_name,
                search: this.searchText,
                filter_min_price: this.filter_min_price,
                filter_max_price: this.filter_max_price,
                filter_free_delivery: free_delivery,
                filter_available: this.filter_available,
                tags: tags,
                page_size: PAGE_LIMIT
            })
                .then(data => {
                    this.catalogCards = data.results
                    console.log('this.catalogCards =>>> ', this.catalogCards);
                    this.currentPage = data.currentPage
                    this.lastPage = data.lastPage
                })
                .then(()=> {
                    this.isCatalogLoaded = true;
                }).catch(() => {
                    console.warn('Ошибка при получении каталога')
                })
        },
    },
    mounted() {
        this.selectedSort = this.sortRules?.[1] ? { ...this.sortRules?.[1], selected: 'inc' } :  null
        this.getCatalogs()
        // this.getTags()
        this.category = location.pathname.startsWith('/catalog/')
            ? Number(location.pathname.replace('/catalog/', ''))
            : null
    },
    data() {
        return {
            pages: 1,
            category: null,
            catalogCards: [],
            currentPage: null,
            lastPage: 1,
            selectedSort: null,
            // search_name: '',
            filter_min_price: 1,
            filter_max_price: 200000,
            filter_free_delivery: false,
            filter_available: true
        }
    }
}